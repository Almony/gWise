from core import on_message
from pyrogram import Client, filters
from pyrogram.types import Message

from features.subscription.middlewares import check_subscription
from features.channel.analyzer.analyzer import ChannelAnalyzer
from core.handlers.exception_handlers import handle_exceptions


@on_message(filters.command("analyzer_on"))
@handle_exceptions
@check_subscription
async def analyzer_on_handler(client: Client, message: Message):
    chat_id = message.chat.id
    analyzer = ChannelAnalyzer(chat_id, client)

    if not await analyzer.is_bot_admin():
        await message.reply_text("❌ Бот должен быть администратором канала для сбора статистики.")
        return

    await analyzer.enable()
    await analyzer.bootstrap_collect_history()
    await message.reply_text("✅ Сбор статистики включён. Исторические данные будут собраны.")


@on_message(filters.command("analyzer_off"))
@handle_exceptions
@check_subscription
async def analyzer_off_handler(client: Client, message: Message):
    chat_id = message.chat.id
    analyzer = ChannelAnalyzer(chat_id, client)

    await analyzer.disable()
    await message.reply_text("📴 Сбор статистики отключён.")


@on_message(filters.command("analyzer_report"))
@handle_exceptions
@check_subscription
async def analyzer_report_handler(client: Client, message: Message):
    chat_id = message.chat.id
    analyzer = ChannelAnalyzer(chat_id, client)

    if not await analyzer.is_enabled():
        await message.reply_text("ℹ️ Сбор статистики не активен. Используй /analyzer_on для запуска.")
        return

    report = await analyzer.generate_report()
    # Placeholder — здесь позже можно форматировать красивый текст
    await message.reply_text(f"📊 Краткий отчёт:\n\n{report or 'Нет данных.'}")
