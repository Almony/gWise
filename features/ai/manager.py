import httpx
from core.config import settings
from core.base import BaseManager
from features.subscription import subscription_manager

class AIManager(BaseManager):
    def __init__(self):
        super().__init__("AIManager")
        self.api_key = settings.OPENAI_API_KEY
        self.url = "https://api.openai.com/v1/chat/completions"

    async def send_request(self, user_id: int, prompt: str, category: str = "general"):
        from core.mongo import UsersRepository  # импорт здесь, чтобы избежать циклов
        user = await UsersRepository.get_user(user_id)
        subscription = user.get("subscription", {})
        sub_type = subscription.get("type", "free")
        months_limit = subscription_manager.get_month_limit(sub_type)

        system_prompt = (
            f"Ты — AI-ассистент категории {category}. "
            f"У пользователя подписка {sub_type}, доступно до {months_limit} мес. данных."
        )

        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.url, json=payload, headers=headers, timeout=30)
                response.raise_for_status()
                data = response.json()

                reply = data["choices"][0]["message"]["content"]
                tokens_used = data.get("usage", {}).get("total_tokens", 0)

                await self.get_collection("ai_requests").insert_one({
                    "user_id": user_id,
                    "prompt": prompt,
                    "category": category,
                    "response": reply,
                    "tokens_used": tokens_used
                })

                if tokens_used > 0:
                    await subscription_manager.decrement_tokens(user_id, tokens_used)
                    self.logger.debug(f"{tokens_used} токенов списано у {user_id}")

                return reply

            except Exception as e:
                self.logger.error(f"AI error: {str(e)}")
                return "Произошла ошибка при обращении к AI. Попробуйте позже."

ai_manager = AIManager()
