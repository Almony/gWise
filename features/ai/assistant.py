# gWise/features/ai/assistant.py

import openai
from datetime import datetime
from core.mongo.schemas.ai_request_schema import AIRequestSchema

class AIClient:
    def __init__(self, api_key: str, mongo_wrapper, logger, model: str = "gpt-4"):
        self.api_key = api_key
        self.mongo_wrapper = mongo_wrapper
        self.logger = logger
        self.model = model

        openai.api_key = self.api_key

    async def ask_gpt(self, user_id: int, prompt: str) -> str:
        """
        Отправляет промпт в OpenAI и возвращает сгенерированный ответ.
        """
        try:
            response = await self._request_openai(prompt)

            reply_text = response["choices"][0]["message"]["content"]
            total_tokens = response["usage"]["total_tokens"]
            model_used = response["model"]

            # Логируем запрос в БД
            ai_request = AIRequestSchema(
                user_id=user_id,
                prompt=prompt,
                response=reply_text,
                total_tokens=total_tokens,
                model_used=model_used,
                created_at=datetime.utcnow()
            )

            await self.mongo_wrapper.insert_one("ai_requests", ai_request.dict())

            return reply_text

        except openai.error.OpenAIError as e:
            self.logger.error(f"Ошибка OpenAI: {e}")
            raise

    async def _request_openai(self, prompt: str) -> dict:
        """
        Низкоуровневая отправка запроса в OpenAI.
        """
        response = await openai.ChatCompletion.acreate(
            model=self.model,
            messages=[
                {"role": "system", "content": "Ты профессиональный AI-ассистент, помоги пользователю."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response
