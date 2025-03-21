#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from tkinter import *


class JogarDados(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.label = Label(master, font=("times", 250))
        button = Button(master, text="Jogar Dados", command=self.jogar)
        button.place(x=200, y=250)

    def jogar(self):
        symbols = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
        self.label.config(text=f"{random.choice(symbols)}{random.choice(symbols)}")
        self.label.pack()


if __name__ == "__main__":
    root = Tk()
    root.title("Jogo de dados")
    root.geometry("500x300")
    JogarDados(root)
    root.mainloop()
