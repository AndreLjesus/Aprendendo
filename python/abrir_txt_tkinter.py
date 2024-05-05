#imports
from tkinter import *
from tkinter import filedialog
from pypdf import PdfReader###

#comando buscar livro
def buscarLivro():
    #buscar aquivo .txt no diretorio downloads
    filename = filedialog.askopenfilename(initialdir = "C:/Users/angel/Downloads", title="Select a File", filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    label_file_explorer.configure(text="File Opened: "+filename)

    #abrir texto em nova janela
    janelaLivro = Tk()

    livro = open(filename, "r")
    texto = livro.read()#

    textoLivro = Label(janelaLivro, text = texto)
    textoLivro.place(x=10, y=10)

    janelaLivro.mainloop()

#janela principal
janela = Tk()
janela.title("text reader")
janela.geometry("330x250")
janela.config(background="dark gray")

label_file_explorer = Label(janela, text = "File Explorer using Tkinter", width = 100, height = 4, fg = "blue")

button = Button(janela, text="proucure um livro", anchor="center", command=buscarLivro)
button.pack(padx=10, pady=5)

janela.mainloop()
