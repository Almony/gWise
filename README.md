```markdown
# 🤖 Telegram AI Assistant Bot Template

Модульный шаблон для создания Telegram-ботов с Pyrogram, AI-ассистентом и подписочной системой.

## 🚀 Возможности

- 📅 Напоминания и задачи
- 💰 Учёт расходов и доходов
- 👥 Управление группами и каналами
- 🧠 AI-ассистент (GPT) с ограничением по подписке
- 🧾 Поддержка подписок: free, base, advanced, pro
- 🌐 MongoDB для хранения всех данных
- 📦 Расширяемая архитектура и декомпозиция
- 🧪 Поддержка pytest для модульных тестов

## 🛠 Установка

```bash
git clone https://github.com/your-username/your-repo-name.git
cd bot_template
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Создай `.env` файл и добавь туда ключи (см. `.env.example` или `.env` в корне).

## 🧾 Команды

- `/start` — инициализация пользователя и подписка
- `/ai` — общий AI-запрос
- `/ai-finance` — анализ финансов
- `/ai-reminder` — анализ напоминаний
- `/ai-group` — анализ групп

## 🧠 Архитектура

```bash
bot_template/
├── ai/                  # AI-ассистент
├── core/                # Конфиги, логгер, Mongo
├── features/            # Напоминания, финансы, группы
├── handlers/            # Pyrogram-хэндлеры
├── subscription/        # Подписки и лимиты
├── tests/               # Pytest-модули
├── main.py              # Точка входа
├── .env                 # Секреты
├── .gitignore
└── README.md
```

## 📌 TODO

- [ ] Подключить оплату
- [ ] Генерация отчётов
- [ ] Telegram User API (расширение)

## 🧑‍💻 Автор

Разработано с ❤️ и AI.
