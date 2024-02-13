#import
import telebot as tb

bot = tb.TeleBot("6332233970:AAHDxrOHak-Uss-f19_u7-GXypqrJfYq81E",parse_mode=None)

@bot.message_handler(commands=["start", "help", "Help"])
def welcome_mensage(message):
    bot.reply_to(message, "Olá")

bot.polling()