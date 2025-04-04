from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from core import on_message, on_callback_query, CustomLogger

logger = CustomLogger("HelpHandler")

def get_help_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Группы", callback_data="help_groups"),
            InlineKeyboardButton("Напоминания", callback_data="help_reminders")
        ],
        [
            InlineKeyboardButton("Финансы", callback_data="help_finance"),
            InlineKeyboardButton("AI", callback_data="help_ai")
        ]
    ])

@on_message(filters.command("help"))
async def help_handler(client: Client, message: Message):
    await message.reply(
        "🆘 *Выбери раздел, о котором хочешь узнать больше:*",
        reply_markup=get_help_keyboard(),
        parse_mode=ParseMode.MARKDOWN
    )
    logger.info(f"Пользователь {message.from_user.id} запросил /help")

@on_callback_query(filters.regex("^help_"))
async def help_callback_handler(client: Client, callback_query: CallbackQuery):
    data = callback_query.data
    user_id = callback_query.from_user.id

    help_texts = {
        "help_groups": (
            "👥 *Группы и каналы*\n\n"
            "Пакет различных услуг для управления вашими группами:\n"
            "— Фильтры от спама и флуда\n"
            "— Блокировка пользователей\n"
            "— Статистика и аналитика\n"
            "— Запланированные сообщения\n\n"
            "_Пример:_ автоудаление ссылок у новых пользователей."
        ),
        "help_reminders": (
            "⏰ *Напоминания*\n\n"
            "Запланируйте важное событие, и бот сам напомнит в нужное время.\n\n"
            "_Пример:_ `напомни через 3 часа позвонить врачу`"
        ),
        "help_finance": (
            "💰 *Финансы*\n\n"
            "Ведите учёт расходов и доходов, анализируйте траты по категориям.\n"
            "Данные сохраняются в БД для дальнейшей аналитики.\n\n"
            "_Пример:_ `/add 300 еда пицца`"
        ),
        "help_ai": (
            "🤖 *AI Аналитика*\n\n"
            "Используй GPT для анализа постов, групп, финансов и напоминаний.\n"
            "Получи ответы на сложные вопросы в одно касание.\n\n"
            "_Пример:_ `/ai-finance проанализируй расходы за февраль`"
        ),
        "help_back": "🆘 *Выбери раздел, о котором хочешь узнать больше:*"
    }

    if data == "help_back":
        await callback_query.message.edit_text(
            help_texts["help_back"],
            reply_markup=get_help_keyboard(),
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        await callback_query.message.edit_text(
            help_texts.get(data, "Раздел не найден."),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Назад", callback_data="help_back")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )

    await callback_query.answer()
    logger.debug(f"Пользователь {user_id} запросил помощь по разделу: {data}")
