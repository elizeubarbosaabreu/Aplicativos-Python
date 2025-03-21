#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import os
from random import choice

class cor:
	amarelo = '\033[93m' 
	vermelho = '\033[91m'
	azul = '\033[7;96m'
	verde = '\033[92m'
	fim = '\033[m'

def cls(): #para limpar a tela
	os.system('clear')
	
def titulo():
	print('{}\n{:^45}\n{}'.format(cor.azul, 'PEDRA-PAPEL-TESOURA', cor.fim))

def jogar():
	cls()
	titulo()
	print('''FAÇA SUA ESCOLHA:
[1] PEDRA
[2] PAPEL
[3] TESOURA
[Ctrl + C] SAIR
	''')
	escolha = str(input('Digite sua escolha: '))
	
	cls()
	titulo()
	print('3...')
	sleep(1)
	
	cls()
	titulo()
	print('2...')
	sleep(1)
	
	cls()
	titulo()
	print('1...')
	sleep(1)
	
	cls()
	titulo()
	print('PEDRA, PAPEL, TESOURA...')
	sleep(1)
	
	cls()
	titulo()
	
		
	if escolha == '1':
		mao = 'PEDRA'
	if escolha == '2':
		mao = 'PAPEL'
	if escolha == '3':
		mao = 'TESOURA'
	
	lista = ['1', '2', '3']
	computador = choice(lista)	
	
	
	if computador == '1':
		ia = 'PEDRA'
	if computador == '2':
		ia = 'PAPEL'
	if computador == '3':
		ia = 'TESOURA'		
	
	
	if mao == ia:
		print('{}JOGO EMPATADO\nNÓS ESCOLHEMOS {}...{}'.format(cor.amarelo, mao, cor.fim))
	
	if escolha == '1' and computador == '2':
		print('{}VOCÊ PERDEU!!!\nESCOLHI {} E VOCÊ ESCOLHEU {}...{}'.format(cor.vermelho, ia, mao, cor.fim))
	if escolha == '1' and computador == '3':
		print('{}VOCÊ VENCEU!!!\nESCOLHI {} E VOCÊ ESCOLHEU {}...{}'.format(cor.verde, ia, mao, cor.fim))
	if escolha == '2' and computador == '1':
		print('{}VOCÊ VENCEU!!!\nESCOLHI {} E VOCÊ ESCOLHEU {}...{}'.format(cor.verde, ia, mao, cor.fim))
	if escolha == '2' and computador == '3':
		print('{}VOCÊ PERDEU!!!\nESCOLHI {} E VOCÊ ESCOLHEU {}...{}'.format(cor.vermelho, ia, mao, cor.fim))	
	if escolha == '3' and computador == '1':
		print('{}VOCÊ PERDEU!!!\nESCOLHI {} E VOCÊ ESCOLHEU {}...{}'.format(cor.vermelho, ia, mao, cor.fim))
	if escolha == '3' and computador == '2':
		print('{}VOCÊ VENCEU!!!\nESCOLHI {} E VOCÊ ESCOLHEU {}...{}'.format(cor.verde, ia, mao, cor.fim))
		
	sleep(7)

while True:
	jogar()
