#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ConversorOctaHexaBin.py
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

def cls():
	os.system('clear')
 
def titulo():
	print('{:^45}\n'.format('CONVERSOR DE BASES NUMÉRICAS'))
	
def conversor():
	cls()
	titulo()
	
	print('''ESCOLHA UMA BASE PARA QUAL DESEJA CONVERTER:
	[1] PARA OCTA;
	[2] PARA HEXADECIMAL
	[3] PARA BINÁRIO
	[Ctrl+C] PARA SAIR
	''')
	escolha = int(input('QUAL É A SUA ESCOLHA? '))
	
	if escolha == 1:
		e = 'OCTAL'
	elif escolha == 2:
		e = 'HEXADECIMAL'
	elif escolha == 3:
		e = 'BINÁRIO'
	else:
		print('Escolha inválida!!!')
		print('REINICIANDO APP....')
		sleep(3)
		conversor()
				
	num = int(input('QUE VALOR VOCÊ QUER CONVERTER PARA {}?: '.format(e)))
	
	print('-=' * 20)
	if escolha == 1:
		print('{} em OCTAL é {}...'.format(num, oct(num)[2:]))
	elif escolha == 2:
		print('{} em HEXADECIMAL é {}...'.format(num, hex(num)[2:]))
	elif escolha == 3:
		print('{} em BINÁRIO é {}...'.format(num, bin(num)[2:]))
		
	
	print('-=' * 20)
	sleep(7)
c = True
while c:
	conversor()
