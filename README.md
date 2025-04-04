# 🤖 Telegram AI Assistant Bot (v3)

Мощный и масштабируемый Telegram-бот с AI-интеграцией (OpenAI GPT), подписками, MongoDB и модульной архитектурой.

---

## 🚀 Возможности

- 🧠 AI-ассистент с категориями: финансы, группы, напоминания
- 🔐 Подписки с лимитами на токены (Free, Base, Advanced, Pro)
- 🗓 Напоминания с хранением, уведомлениями и архивом
- 💰 Учёт расходов и доходов, с повторяющимися тратами
- 👥 Работа с группами и постами (аналитика, структура)
- 📊 Логирование всех AI-запросов
- 🧪 Pytest-тесты
- ☁️ MongoDB + Pydantic + Asynchronous I/O
- 💡 Расширяемость и чистая архитектура

---

## ⚙️ Установка

```bash
git clone https://github.com/your-name/gWise.git
cd gWise
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Создайте `.env`:
```
API_ID=...
API_HASH=...
BOT_TOKEN=...
MONGODB_URI=mongodb://localhost:27017
OPENAI_API_KEY=...
```

---

## 🗂️ Структура проекта

```
gWise/
├── core/                          # Базовые утилиты
│   ├── __init__.py                # Упрощённый импорт core компонентов
│   ├── base.py                    # BaseManager с логгером и доступом к Mongo
│   ├── config.py                  # Загрузка .env
│   ├── event_router.py            # Роутер событий (on_message, on_callback)
│   ├── logger.py                  # Кастомный логгер
│   └── settings_manager.py        # Глобальные настройки
|
├── core/system/                   #
│   ├── __init__.py                # get_collection, UsersRepository
│   ├── sys_logger.py              # Логирование системных событий в MongoDB
|
├── core/mongo/                   # Работа с MongoDB
│   ├── __init__.py                # get_collection, UsersRepository
│   ├── client.py                  # Mongo-клиент
│   ├── base.py                    # get_collection()
│   ├── users.py                   # Методы по users
│   └── schemas/
│       ├── __init__.py
│       ├── ai.py
│       ├── finance.py
│       ├── group.py
│       ├── reminder.py
│       ├── settings.py
│       ├── system.py
│       └── collections.py

├── features/
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── manager.py
│   │   └── history.py
│   ├── finance/
│   │   ├── __init__.py
│   │   └── manager.py
│   ├── group/
│   │   ├── __init__.py
│   │   └── manager.py
│   ├── reminder/
│   │   ├── __init__.py
│   │   └── manager.py
│   └── subscription/
│       ├── __init__.py
│       ├── manager.py
│       └── middlewares.py

├── handlers/
│   ├── start_handler.py
│   ├── help_handler.py
│   └── ai_handler.py

├── system/
│   └── logger_db.py               # Логирование системных событий в MongoDB

├── infra/
│   └── install_mongo.sh           # Установка MongoDB (опционально)

├── logs/                          # Автоматически создаваемые логи
│
├── tests/                         # Тесты на Pytest
│
├── main.py                        # Точка входа
├── requirements.txt
└── README.md
```

---

## 🧪 Тестирование

```bash
pytest
```

---

## 👨‍💻 Автор
Navapathi
