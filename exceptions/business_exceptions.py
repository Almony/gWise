class BusinessError(Exception):
    """Базовая бизнес-ошибка, которая отображается пользователю."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


# ==== Общие ошибки ====

class AccessDenied(BusinessError):
    def __init__(self):
        super().__init__("Ошибка: доступ запрещён.")

class SubscriptionRequired(BusinessError):
    def __init__(self):
        super().__init__("Ошибка: эта команда доступна только подписчикам.")

class TokenLimitExceeded(BusinessError):
    def __init__(self):
        super().__init__("Ошибка: превышен лимит токенов. Повышайте тариф для продолжения.")

# ==== Напоминания ====

class ReminderNotFound(BusinessError):
    def __init__(self):
        super().__init__("Ошибка: напоминание не найдено. Возможно, оно было удалено.")

class InvalidReminderDate(BusinessError):
    def __init__(self):
        super().__init__("Ошибка: указана некорректная дата для напоминания.")

# ==== GPT / OpenAI ====

class GPTServiceUnavailable(BusinessError):
    def __init__(self):
        super().__init__("Ошибка: не удалось получить ответ от GPT. Попробуйте позже.")

class GPTBadRequest(BusinessError):
    def __init__(self):
        super().__init__("Ошибка: некорректный запрос к GPT.")

# ==== Финансы ====

class CategoryNotFound(BusinessError):
    def __init__(self):
        super().__init__("Ошибка: категория не найдена.")

class NotEnoughBalance(BusinessError):
    def __init__(self):
        super().__init__("Ошибка: недостаточно средств для операции.")
