import telebot
from pic_overlaper import congratulation_func

bot = telebot.TeleBot('YOUR_BOT_TOKEN')


@bot.message_handler(content_types=['text'])
def quote_message_handler(message):
    image_to_send = congratulation_func(message.text)
    bot.send_photo(chat_id=message.chat.id, photo=image_to_send)


def telegram_polling():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    telegram_polling()
