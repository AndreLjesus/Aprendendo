#import
import telebot as tb
from telebot import types

bot = tb.TeleBot("6332233970:AAHDxrOHak-Uss-f19_u7-GXypqrJfYq81E",parse_mode=None)
chat_id_host = 6234485725
user = bot.get_me()

@bot.message_handler(commands=["start", "help", "Help"])
def welcome_mensage(message):
    bot.reply_to(message, "Olá")

@bot.message_handler(commands=["Discord", "discord"])
def discord(message):
    mensagem = "Entre no servidor do Discord: https://discord.gg/ZAr3qbwc"
    bot.reply_to(message, mensagem)
    bot.send_message(chat_id_host, "{} vai entrar no Discord!".format(message.chat.first_name))

@bot.message_handler(commands=["livros"])
def livros(message):
    doc = open('telegram\Maze_Runner_1.epub', 'rb')
    bot.send_document(message.chat.id, doc)
    
bot.polling()