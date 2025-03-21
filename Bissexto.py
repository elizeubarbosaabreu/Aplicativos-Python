#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Autor: Elizeu Barbosa Abreu

# IMPORTAÇÃO DAS BIBLIOTECAS E RECURSOS
from datetime import date
import os
from time import sleep

# DEFINIÇÃO DAS CORES USADAS NO PROJETO
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

# FUNÇÃO PARA LIMPAR A TELA
def cls(): #limpar tela
	os.system('clear')

# FUNÇÃO CALCULAR ANO BISSEXTO
def software():
	# INSERÇÃO DOS VALORES
	ano = int(input('\n{}Digite o ano que deseja analizar se é bissexto: {}'.format(bcolors.FAIL, bcolors.RESET)))
	cls()
	
	print('{}{:^45}{}'.format(bcolors.OK, 'ANO BISSEXTO', bcolors.RESET))
	print('\nFOLHEANDO CALENDÁRIO...')
	sleep(2)
	cls()
	
	print('{}{:^45}{}'.format(bcolors.OK, 'ANO BISSEXTO', bcolors.RESET))
	print('\nAGUARDE MAIS UM POUQUINHO...')
	sleep(2)
	cls()
	
	print('{}{:^45}{}'.format(bcolors.OK, 'ANO BISSEXTO', bcolors.RESET))
	print('\nAGORA VAI...')
	sleep(2)
	cls()
	
	print('{}{:^45}{}'.format(bcolors.OK, 'ANO BISSEXTO', bcolors.RESET))
	
	# CONDICIONAL PARA ALGORÍTMO DE CALCULO DE ANO BISSEXTO
	# PARA SER BISSEXTO, O ANO DEVE SER:
	# *DIVISÍVEL POR 4. SENDO ASSIM, A DIVISÃO É EXATA COM O RESTO IGUAL A ZERO; [ano % 4 == 0]
	# *NÃO PODE SER DIVISÍVEL POR 100. COM ISSO, A DIVISÃO NÃO É EXATA, OU SEJA, DEIXA RESTO DIFERENTE DE ZERO; [ano % 100 != 0]
	# *PODE SER QUE SEJA DIVISÍVEL POR 400. CASO SEJA DIVISÍVEL POR 400, A DIVISÃO DEVE SER EXATA, DEIXANDO O RESTO IGUAL A ZERO. [ano % 400 == 0]
	# FONTE: HTTPS://ESCOLAKIDS.UOL.COM.BR/MATEMATICA/CALCULO-DO-ANO-BISSEXTO.HTM
	if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
		print('\nO ano {} é {}BISSEXTO{}!'.format(ano, bcolors.OK, bcolors.RESET))
	else:
		print('\nO ano {} {}NÃO É BISSEXTO{}!'.format(ano, bcolors.FAIL, bcolors.RESET))
	
	sleep(5)
	cls()
	
	print('{}{:^45}{}'.format(bcolors.OK, 'ANO BISSEXTO', bcolors.RESET))
	print('\nPREPARANDO NOVA ANÁLISE...')
	sleep(2)
	cls()

c = True
while c:
	print('{}{:^45}{}'.format(bcolors.OK, 'ANO BISSEXTO', bcolors.RESET))
	print('\n{}Este aplicativo verifica se um ano é bissexto ou não!!!{}'.format(bcolors.WARNING, bcolors.RESET))
	software()
