import telebot

bot = telebot.TeleBot("1210902697:AAFo3R-MS3Z3xZEnX7o0CaGNrU4gV5vc0rg")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.reply_to(message, message.text)

bot.polling( none_stop = True )
