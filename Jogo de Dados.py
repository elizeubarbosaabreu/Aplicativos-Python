#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Jogo de Dados.py
#  
#  Copyright 2021 Elizeu Barbosa Abreu <elizeubcorreios@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import random
from tkinter import *

class JogarDados(object):
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.label = Label(master, font=('times', 250))
		button = Button(master, text='Jogar Dados', command=self.jogar)
		button.place(x=200, y=10)

	def jogar(self):
		symbols = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
		self.label.config(text=f'{random.choice(symbols)}{random.choice(symbols)}')
		self.label.pack()

if __name__ == '__main__':
	root = Tk()
	root.title('Jogo de dados')
	root.geometry('500x300')
	JogarDados(root)
	root.mainloop()
