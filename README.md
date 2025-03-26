# 🤖 Telegram AI Assistant Bot Template

Модульный шаблон для создания Telegram-ботов на Pyrogram с AI-ассистентом (GPT), MongoDB, логированием и системой подписок.

---

## 🚀 Возможности

- 📅 Напоминания и задачи
- 💰 Учёт расходов и доходов
- 👥 Управление группами и каналами
- 🧠 AI-ассистент (GPT) с ограничением по подписке
- 🧾 Поддержка подписок: free, base, advanced, pro
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

### 🔹 Создание и активация виртуального окружения

```bash
python3 -m venv venv
source venv/bin/activate    # для Linux/macOS
venv\Scripts\activate.bat # для Windows
```

### 🔹 Установка зависимостей

```bash
pip install -r requirements.txt
```

---

## 🔑 Настройка `.env`

Создайте файл `.env` в корне проекта со следующим содержимым:

```dotenv
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
MONGODB_URI=mongodb://localhost:27017
OPENAI_API_KEY=your_openai_api_key
```

---

## 🧭 Структура проекта

```
bot_template/
├── ai/
│   └── ai_manager.py                # Обработка AI-запросов через OpenAI API
├── core/
│   ├── config.py                    # Загрузка переменных окружения
│   ├── logger.py                    # Кастомный логгер
│   └── mongo_manager.py             # Обёртка для работы с MongoDB
├── features/
│   ├── reminder_manager.py          # Управление напоминаниями
│   ├── finance_manager.py           # Учёт финансов
│   └── group_manager.py             # Управление группами и настройками
├── subscription/
│   └── subscription_manager.py      # Подписки и контроль лимитов
├── handlers/
│   ├── start_handler.py             # Обработка команды /start
│   ├── ai_handler.py                # Обработка /ai и подобных команд
│   └── common.py                    # Общие утилиты и декораторы
├── tests/
│   └── test_start.py                # Базовые автотесты
├── logs/                            # Логи (создаются автоматически)
├── main.py                          # Точка входа, инициализация клиента Pyrogram
├── .env                             # Секреты и конфигурация
├── .gitignore                       # Исключения для git
├── README.md                        # Документация
└── requirements.txt                 # Зависимости проекта
```

---

## 🧪 Тестирование

```bash
pytest
```

---

## 🐳 Docker (опционально)

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
```

---

## ⚙️ CI (GitHub Actions пример)

```yaml
# .github/workflows/python-tests.yml
name: Pytest

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
```

---

## 📌 TODO

- [ ] Интеграция оплаты
- [ ] Рассылки по подпискам
- [ ] AI-отчёты и PDF/Excel генерация
- [ ] Планировщик уведомлений

---

## 🧑‍💻 Автор

Разработано с ❤️ и AI.
