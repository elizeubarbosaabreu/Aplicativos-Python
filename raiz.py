#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt # FUNÇÃO DE RAIZ
from time import sleep

def raiz():
	while True:
		num = int(input('Escreva um número: '))
		if num < 0:
			print(f'O número {num} não possui raíz quadrada por ser negativo!!!\nBye!')
			break
		print('A raiz quadrada de \033[91m{:.2f}\033[m é \033[92m{:.2f}\033[m \n\n'.format(num, sqrt(num)))
		sleep(5)


raiz()
	
	
