from tkinter import *
import main
from PIL import Image, ImageTk
import os

def cifrar_mensagem():
    mensagem = mensagem_entry.get()
    chave = chave_entry.get()
    cifrada = main.cifra_vigenere(mensagem, chave)
    resultado_label["text"] = f"Palavra cifrada: {cifrada}"

def decifrar_mensagem():
    cifrada = mensagem_entry.get()
    chave = chave_entry.get()
    decifrada = main.decifrar_vigenere(cifrada, chave)
    resultado_label["text"] = f"Palavra decifrada: {decifrada}"

# Cria a janela principal
janela = Tk()
janela.title("Cifra Polialfabética")
janela.geometry("240x140")
janela.resizable(False, False)

# Cria os widgets
mensagem_label = Label(janela, text="Frase:")
mensagem_entry = Entry(janela)
chave_label = Label(janela, text="Chave:")
chave_entry = Entry(janela)
resultado_label = Label(janela, text="")

cifrar_button = Button(janela, text="Cifrar", command=cifrar_mensagem, width=10)
decifrar_button = Button(janela, text="Decifrar", command=decifrar_mensagem, width=10)

# Define a posição dos widgets na janela
mensagem_label.grid(row=0, column=0)
mensagem_entry.grid(row=0, column=1)
chave_label.grid(row=1, column=0)
chave_entry.grid(row=1, column=1)
resultado_label.grid(row=2, column=0, columnspan=10, pady=5)
cifrar_button.place(x=10, y=90)
decifrar_button.place(x=120, y=90)

# Inicia o loop principal da janela
janela.mainloop()
