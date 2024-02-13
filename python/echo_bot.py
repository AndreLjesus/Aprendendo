#Todos os imports do programa
import telebot as tb
from telebot import types

#Variaveis gerais
bot = tb.TeleBot("6332233970:AAHDxrOHak-Uss-f19_u7-GXypqrJfYq81E",parse_mode=None)
chat_id_host = 6234485725

#Lista com o nome de todos os livros disponiveis
lista = ["Maze Runner"]

#Comando se Start / Help
@bot.message_handler(commands=["start", "help", "Help"])
def welcome_mensage(message):
    bot.reply_to(message, "Olá")

#Comando do Discord
@bot.message_handler(commands=["Discord", "discord"])
def discord(message):
    mensagem = "Entre no servidor do Discord: https://discord.gg/ZAr3qbwc"
    bot.reply_to(message, mensagem)
    bot.send_message(chat_id_host, "{} vai entrar no Discord!".format(message.chat.first_name))

#Comando para proucurar livros
@bot.message_handler(commands=["livro"])
def livros(message):
    titulo = bot.send_message(message.chat.id, "Qual o livro?... ")
    bot.register_next_step_handler(titulo, Titulo)

def Titulo(message):
    open("titulo.txt", "w").write(message.text)
    bot.send_message(message.chat.id, "Procurando!")
    def MazeRunner():
        doc = open('telegram\Maze_Runner_1.epub', 'rb')
        bot.send_document(message.chat.id, doc)
        doc = open('telegram\Maze_Runner_2.epub', 'rb')
        bot.send_document(message.chat.id, doc)
    if message.text == "Maze Runner":
        MazeRunner()
    else:
        bot.send_message(message.chat.id, "Livro não encontrado!")

bot.polling()