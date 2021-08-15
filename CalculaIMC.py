#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CalculaIMC.py
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

def title():
	print('\n{}{:^72}{}\n'.format('\033[7;96m', 'CALCULADORA IMC', '\033[m'))

def calculoimc():
	cls()
	title()
	
	peso = float(input('Entre com seu peso: '))
	altura = float(input('Entre com sua altura: '))
	imc = peso/pow(altura, 2)
	cls()
	title()
	print('CALCULANDO...')
	sleep(2)
	cls()
	
	title()
	
	if imc < 18.5:
		print('IMC: {:.2f} ---> ABAIXO DO PESO'.format(imc))
	elif imc < 25:
		print('IMC: {:.2f} ---> PESO IDEAL'.format(imc))
	elif imc < 30:
		print('IMC: {:.2f} ---> SOBREPESO'.format(imc))
	elif imc < 35:
		print('IMC: {:.2f} ---> OBESIDADE GRAU I'.format(imc))
	elif imc < 40:
		print('IMC: {:.2f} ---> OBESIDADE GRAU II'.format(imc))
	else:
		print('IMC: {:.2f} ---> OBESIDADE GRAU III OU MÓRBIDA'.format(imc))
	print('\nPressione CTRL+C se quiser sair...\nAguarde para fazer novo cálculo...')	
	sleep(7)
	
while True:
	calculoimc()

