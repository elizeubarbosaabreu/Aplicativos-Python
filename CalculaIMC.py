#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

