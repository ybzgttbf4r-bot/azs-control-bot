import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN is not set. Add it in Render Environment Variables.")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")


def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("📍 Найти АЗС")
    keyboard.row("✍️ Сообщить обстановку")
    keyboard.row("🎁 Мои бонусы")
    return keyboard


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "⛽ <b>АЗС Контроль</b>\n\n"
        "Сервис для проверки очередей и наличия топлива на АЗС.\n\n"
        "Выбери действие:",
        reply_markup=main_menu()
    )


@bot.message_handler(func=lambda message: message.text == "📍 Найти АЗС")
def find_azs(message):
    bot.send_message(
        message.chat.id,
        "📍 <b>Ближайшие АЗС</b>\n\n"
        "Пока тестовый режим:\n\n"
        "🟢 Роснефть — очередь 5–10 мин, 95 есть\n"
        "🟡 Лукойл — очередь 15 мин, 92/95 есть\n"
        "🔴 Газпромнефть — бензина нет\n\n"
        "Скоро подключим реальные данные и геолокацию."
    )


@bot.message_handler(func=lambda message: message.text == "✍️ Сообщить обстановку")
def report(message):
    bot.send_message(
        message.chat.id,
        "✍️ Напиши сообщение в таком формате:\n\n"
        "<b>Город, адрес АЗС, очередь, топливо</b>\n\n"
        "Пример:\n"
        "Питер, Выборгское шоссе 222, очередь 15 минут, 95 есть"
    )


@bot.message_handler(func=lambda message: message.text == "🎁 Мои бонусы")
def bonuses(message):
    bot.send_message(
        message.chat.id,
        "🎁 <b>Мои бонусы</b>\n\n"
        "Баланс: 0 литров\n"
        "Сообщений: 0\n\n"
        "Скоро за полезные сообщения будут начисляться виртуальные литры."
    )


@bot.message_handler(content_types=["text"])
def any_text(message):
    bot.send_message(
        message.chat.id,
        "✅ Принял сообщение.\n\n"
        "В следующей версии будем сохранять такие сообщения в базу."
    )


if __name__ == "__main__":
    print("АЗС Контроль запущен")
    bot.infinity_polling(skip_pending=True)
