# 🤖 Telegram AI Assistant Bot (v2)

Мощный и масштабируемый Telegram-бот с AI-интеграцией (GPT), подписками, MongoDB и модульной архитектурой.

---

## 🚀 Возможности

- 🧠 AI-ассистент с категориями и ограничениями по подписке
- 🗓 Напоминания с временем, хранением и планируемыми уведомлениями
- 💰 Учёт расходов/доходов
- 👥 Поддержка чатов и групп (в разработке)
- 📊 История запросов и транзакций
- 🧪 Тестирование через `pytest`
- 🔐 Подключение через `.env`, логирование и безопасная структура
- 💡 Расширяемость: легко добавлять новые фичи

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
├── ai/
│   ├── ai_manager.py              # Взаимодействие с OpenAI API (GPT), логика запросов
│   └── history_manager.py         # Логирование AI-запросов в MongoDB
│
├── core/
│   ├── config.py                  # Загрузка переменных окружения (.env)
│   ├── event_roter.py            # Роутер событий (сообщения, callback-и, редактирования)
│   ├── logger.py                  # Кастомный логгер с file+console выводом
│   ├── settings_manager.py        # Хранение и управление глобальными настройками
│   └── mongo/
│       ├── mongo_manager.py       # Работа с MongoDB, пользователями, коллекциями
│       └── schemas.py             # Pydantic-схемы для всех коллекций MongoDB
│
├── features/
│   ├── reminder/
│   │   └── reminder_manager.py    # Создание, хранение, архивирование напоминаний
│   │                              # Поддержка повторяющихся событий, статусов
│   ├── finance/
│   │   └── finance_manager.py     # Учёт транзакций, категории, повторы, фильтрация
│   ├── subscription/
|   |   ├── middlewares.py           # subscription midlewares
│   │   └── subscription_manager.py    # Подписки (free/base/pro), лимиты, приоритеты, декоратор
│   └── group/
│       └── group_manager.py       # Группы: добавление, участники, посты, активность
│
├── handlers/
│   ├── start_handler.py           # Команда /start, приветствие и первичное создание пользователя
│   ├── help_handler.py            # Интерактивное меню помощи с кнопками и подробностями
│   └── ai_handler.py              # Категориальные AI-команды: /ai, /ai-finance, /ai-reminder, /ai-group
│
├── system/
│   └── logger_db.py                   # Запись системных событий в MongoDB
|
├── infra/
│   └── install_mongo.sh           # Скрипт установки MongoDB (опционально)
│
├── logs/                          # Директория для логов: bot.log и модульные логи
│
├── tests/                         # Pytest-тесты (в разработке)
│
├── main.py                        # Точка входа: запуск Pyrogram-клиента, регистрация всех хендлеров
├── requirements.txt               # Зависимости проекта
└── README.md                      # Документация

```

---

## 🧪 Тестирование

```bash
pytest
```

---

## 👨‍💻 Автор
Navapathi
