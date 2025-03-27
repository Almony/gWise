# 🤖 Telegram AI Assistant Bot Template

🔹 Модульный шаблон Telegram-бота на Pyrogram с AI (GPT), MongoDB, логированием и подписками.

---

## 🚀 Возможности

- 🗓️ Напоминания и задачи
- 💰 Учёт расходов и доходов
- 👥 Управление группами и каналами
- 🧠 AI-ассистент (GPT) с ограничением по подписке
- 📜 Поддержка подписок: free, base, advanced, pro
- 🌐 MongoDB для хранения всех данных
- 🧪 Поддержка pytest для модульных тестов
- 📦 Расширяемая архитектура и модульность

---

## ⚙️ Установка

### 🔹 Клонирование репозитория
```bash
git clone git@github.com:Almony/t-assist.git
cd t-assist
```

### 🔹 Виртуальное окружение
```bash
python3 -m venv venv
source venv/bin/activate  # для Linux/macOS
venv\Scripts\activate.bat # для Windows
```

### 🔹 Установка зависимостей
```bash
pip install -r requirements.txt
```

---

## 🔑 Настройка `.env`
Создайте файл `.env`:
```
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
MONGODB_URI=mongodb://localhost:27017
OPENAI_API_KEY=your_openai_api_key
```

---

## 🔎 Структура проекта
```
bot_template/
├── ai/
│   └── ai_manager.py
├── core/
│   ├── config.py
│   ├── logger.py
│   └── mongo_manager.py
├── features/
│   ├── reminder_manager.py
│   ├── finance_manager.py
│   └── group_manager.py
├── subscription/
│   └── subscription_manager.py
├── handlers/
│   ├── start_handler.py
│   ├── ai_handler.py
│   └── common.py
├── tests/
├── logs/
├── main.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🧪 Тестирование
```bash
pytest
```

---

## 💪 TODO

### 📉 Безопасность и валидация
- [ ] Валидация входных данных (`user_id`, `prompt`, `amount`, `due_time`, `category`)
- [ ] Обработка `None`/пустых `user.subscription`
- [ ] Безопасный JSON-парсинг ответа от OpenAI
- [ ] Retry-механизм при ошибках OpenAI API

### 🤔 Тестирование
- [ ] Расширить unit-тесты для AI, подписок, финансов, напоминаний
- [ ] Проверка, что данные действительно сохраняются в MongoDB

### 🏛️ Архитектура
- [ ] Dependency Injection для `MongoManager`, `Logger`
- [ ] Утилиты: `sanitize_input()`, `safe_mongo_call()`, `retry_async()`

### ⏰ Планировщик
- [ ] Интеграция `apscheduler` для напоминаний
- [ ] Отметка `notified` с логированием ошибок

### 💳 Подписки и платежи
- [ ] Интеграция Telegram Payments или Stripe
- [ ] Webhook-обновления подписки
- [ ] Уведомления о лимите или окончании срока

### 📄 Отчёты и экспорт
- [ ] Генерация AI-отчётов в PDF/Excel

---

## 🚩 CI/CD (GitHub Actions)
```yaml
name: Pytest

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest
```

---

## 👨‍💻 Автор
Разработано с ❤️ и AI.

