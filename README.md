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
ADMIN_LOG_CHAT_ID=12345
ADMIN_IDS=12345,54321,234124
DEV_IDS=12345,54321,123421
```

---

## 🗂️ Структура проекта

```
gWise/
├── features/                  # Основные бизнес-фичи бота, разбиты по модулям
│   ├── ai/                    # AI-интеграция (OpenAI, история запросов)
│   │   ├── manager.py         # Логика обработки AI-запросов
│   │   ├── history.py         # Управление историей AI-запросов
│   │   └── __init__.py
|   |
│   ├── finance/               # Финансовый модуль (учет, категории и т.п.)
│   │   ├── manager.py
│   │   └── __init__.py
|   |
│   ├── group/                 # Управление группами и их настройками
│   │   ├── manager.py
│   │   └── __init__.py
|   |
│   ├── reminder/              # Напоминания (создание, хранение, проверка)
│   │   ├── manager.py
│   │   └── __init__.py
|   |
│   ├── subscription/          # Система подписок и ограничений
│   │   ├── manager.py
│   │   ├── middlewares.py     # Middleware для проверки лимитов и доступа
│   │   └── __init__.py
|   |
│   └── system/
│       └── logger_manager.py  # Менеджер логгирования
│
├── core/                      # Инфраструктурные и базовые компоненты
│   ├── system/
│   │   ├── config.py          # Конфигурация проекта
│   │   ├── event_router.py    # Центральный router событий (Pyrogram)
│   │   └── __init__.py
|   |
│   ├── mongo/                 # Работа с MongoDB
│   │   ├── client.py          # Инициализация подключения
│   │   ├── users.py           # Обработка запросов к коллекции пользователей
│   │   ├── base.py            # Базовые модели и утилиты
|   |   ├── __init__.py
|   |   |
│   │   ├── schemas/           # Схемы коллекций
│   │   │   ├── ai.py
│   │   │   ├── collections.py
│   │   │   ├── finance.py
│   │   │   ├── group.py
│   │   │   ├── reminder.py
│   │   │   ├── settings.py
│   │   │   ├── system.py
│   │   │   └── user.py
|   |
│   ├── logging/               # Расширенное логгирование
│   │   ├── logger.py
│   │   ├── sys_logger.py
│   │   ├── telegram_reporter.py  # Отправка ошибок в Telegram
│   │   ├── logging_config.py
│   │   └── __init__.py
|   |
│   ├── handlers/              # Обработка исключений
│   │   ├── exception_handlers.py
│   │   └── __init__.py
|   |
│   ├── retry.py               # Повторные попытки (retry logic)
│   ├── base.py                # Базовые интерфейсы и утилиты
│   ├── setings_manager.py     # Менеджер глобальных настроек
│   └── __init__.py
│
├── exceptions/                # Кастомные бизнес-исключения
│   ├── business_exceptions.py
│   └── __init__.py
│
├── infra/                     # Инфраструктура проекта
│   └── install_mongo.sh       # Скрипт установки MongoDB
│
├── handlers/                  # Хэндлеры Telegram-команд
│   ├── start_handler.py
│   ├── help_handler.py
│   └── ai_handler.py
│
├── tests/                     # Pytest-тесты
│   ├── test_ai.py
│   ├── test_subscription.py
│   └── test_start.py
│
├── main.py                    # Точка входа, запуск бота
├── requirements.txt           # Зависимости проекта
├── .gitignore                 # Игнорируемые файлы для Git
└── README.md                  # Документация проекта


```

---

## 🧪 Тестирование

```bash
pytest
```

---

## 👨‍💻 Автор
Navapathi
