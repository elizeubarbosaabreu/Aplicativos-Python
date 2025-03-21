#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Advinhe o Numero.py
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
from time import sleep
import os
from random import randint

def cls():
	os.system('clear')

def titulo():
	print('{}{:^50}{}'.format('\033[7m', 'JOGO ADVINHE O NÚMERO', '\033[m'))

def game():
	count = 0
	humano = 1000
	computador = randint(1, 100)
	# primeira pagina
	cls()
	titulo()
	nome = str(input('''
Olá sou a I.A. mais conhecida como Inteligência artificial.
Vou pensar em um número e espero que você advinhe na menor quantidade de tentativas...
Mais antes quero saber um pouco mais sobre você...

>>>> Qual é o seu nome? '''))

# segunda página
	cls()
	titulo()
	
	humano = int(input(f'''
Olá {nome}, que bom te conhecer...
Pensei em um número entre 0 e 100...
Tente advinhar o número que pensei!!!
Espero que você acerte na primeira tentativa!!!

>>>> Digite o número que pensei: '''))

	while humano != computador:
		if humano > computador:
			humano = int(input(f'\n{nome}, não foi desta vez!\nTente outro número menor: '))
			count += 1
		if humano < computador:
			humano = int(input(f'\n{nome}, não foi desta vez!\nTente outro número maior: '))
			count += 1
	else:
		count += 1
		print(f'''
Parabéns {nome},
Você acertou em {count} tentativas!!!''')

while True:
	game()
	sleep(7)
	cls()
	titulo()
	print('\nQuando quiser sair tecle [ctrl+C]...')
	sleep(2)
