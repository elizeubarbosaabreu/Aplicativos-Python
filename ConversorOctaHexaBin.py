#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
