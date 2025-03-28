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
git clone https://github.com/your-name/t-assist.git
cd t-assist
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
bot_template/
├── ai/
│   └── ai_manager.py             # Логика общения с OpenAI
│
├── core/
│   ├── config.py                 # Настройки из .env
│   ├── logger.py                 # Кастомный логгер
│   └── mongo_manager.py          # Работа с MongoDB (motor)
│
├── features/
│   ├── reminder/
│   │   └── manager.py            # Напоминания: добавление, проверка, отметка
│   ├── finance/
│   │   └── manager.py            # Финансы: транзакции, фильтрация
│   └── group/
│       └── manager.py            # Заготовка для работы с группами
│
├── subscription/
│   └── subscription_manager.py    # Управление подписками и декоратор
│
├── handlers/
│   ├── start/
│   │   └── start_handler.py          # Команда /start
│   ├── help/
│   │   └── help_handler.py            # меню помощи и гайд пользователя
│   └── ai/
│       └── ai_handler.py             # Обработка AI-команд с категориями
│
├── tests/
│   ├── test_start.py
│   ├── test_ai.py
│   ├── test_finance.py
│   ├── test_reminder.py
│   └── test_subscription.py
│
├── main.py                       # Точка входа, запуск Pyrogram-клиента
├── requirements.txt
└── README.md
```

---

## 🧪 Тестирование

```bash
pytest
```

---

## 🛠 TODO / Roadmap

### 🌐 Архитектура
- [ ] Dependency Injection (Mongo, Logger)
- [ ] Хэндлеры и менеджеры вынести в отдельные подпапки при необходимости

### 🤖 AI-интеграция
- [ ] Retry + safe parse
- [ ] Генерация AI-отчётов

### ⏰ Напоминания
- [ ] Планировщик (apscheduler)
- [ ] Уведомления

### 💳 Подписки
- [ ] Telegram Payments / Stripe
- [ ] Рассылки о лимитах

---



---

## 👨‍💻 Автор
Navapathi
