import httpx
from core.config import settings
from core.mongo_manager import MongoManager
from subscription.subscription_manager import subscription_manager
from core.logger import CustomLogger

logger = CustomLogger("AIManager")

class AIManager:
    def __init__(self):
        self.mongo = MongoManager()
        self.api_key = settings.OPENAI_API_KEY
        self.url = "https://api.openai.com/v1/chat/completions"

    async def send_request(self, user_id: int, prompt: str, category: str = "general"):
        user = await self.mongo.get_user(user_id)
        subscription = user.get("subscription", {})
        months_limit = subscription_manager.get_month_limit(subscription.get("type", "free"))

        # Добавим в prompt мета-информацию
        system_prompt = f"Ты — AI-ассистент категории {category}. У пользователя подписка {subscription.get('type')}, доступно до {months_limit} мес. данных."

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

                # Сохраняем в истории
                await self.mongo.get_collection("ai_requests").insert_one({
                    "user_id": user_id,
                    "prompt": prompt,
                    "category": category,
                    "response": reply
                })

                return reply

            except Exception as e:
                logger.error(f"AI error: {str(e)}")
                return "Произошла ошибка при обращении к AI. Попробуйте позже."

ai_manager = AIManager()
