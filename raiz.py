#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  raiz.py
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
	
	
