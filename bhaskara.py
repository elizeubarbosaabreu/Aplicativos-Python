#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bhaskara.py
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

# IMPORTAÇÃO DAS BIBLIOTECAS
from time import sleep
from math import sqrt
import os

# DECLARAÇÃO DAS FUNÇÕES

# FUNÇÃO PARA LIMPAR TELA
def cls():
	os.system('clear')

# FUNÇÃO PARA IMPRIMIR O TÍTULO CENTRALIZADO E COM
# CORES INVERTIDAS	
def titulo():
	print('{}{:^45}{}'.format('\033[7m', 'FÓRMULA DE BHASKARA', '\033[m'))

# FUNÇÃO PARA CALCULAR DELTA
def delta(a, b, c):
	delta = pow(b, 2) - 4 * a * c
	return delta

# FUNÇÃO PARA CALCULAR X1	
def x1(a, b, c, delta):
	x1 = (-b + sqrt(delta))/(2 * a)
	return x1
	
# FUNÇÃO PARA CALCULAR X1	
def x2(a, b, c, delta):
	x2 = (-b - sqrt(delta))/(2 * a)
	return x2

# CHAMADA PARA EXECUTAR O ALGORITMO ENQUANTO TRUE. NO CASO DELTA FOR MAIOR
# QUE ZERO

while True:
	cls()
	titulo()

	# ENTRADA DOS VALORES	
	a = float(input('Entre com o valor de A: '))
	b = float(input('Entre com o valor de B: '))
	c = float(input('Entre com o valor de C: '))
	
	if a < 0:
		a1 = str(a)
	else:
		a1 = '+' + str(a)

	if b < 0:
		b1 = str(b)
	else:
		b1 = '+' + str(b)
		
	if c < 0:
		c1 = str(c)
	else:
		c1 = '+' + str(c)

	# CALCULOS E EXIBIÇÃO DOS VALORES
	print('\n\nNa Equação do 2º grau \033[7m{}x²{}x{}=0\033[m'.format(a1, b1, c1), end=' ')

	delta = delta(a, b, c)
		
	print('Delta é \033[7m{}\033[m,'.format(delta), end=' ')
	if delta < 1:
		print('Delta menor que 1. Resolução impossível!!!')
		break

	x1 = x1(a, b, c, delta)
	print('X1 é \033[7m{:2.2f}\033[m'.format(x1), end=' e ')

	x2 = x2(a, b, c, delta)
	print('X2 é \033[7m{:2.2f}\033[m...'.format(x2))

	print('\n\n\nDigite [Ctrl+c] ou aguarde 15 segundos para novo cálculo...')
	sleep(15)
