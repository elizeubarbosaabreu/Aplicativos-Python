# coding=UTF-8

# INSERÇÃO DOS VALORES
num = []
qt_num = int(input('Quantos números você quer digitar? '))

# FUNÇÃO QUE RECEBE OS VALORES
def maior_menor(num, qt_num):    
    for count in range(qt_num):
        n = int(input('Entre com um número: '))
        num.append(n)
    maior = max(num)
    menor = min(num)
    print('{:^6}|{:^5}'.format('INDICE', 'VALOR'))
    for x, y in enumerate(num):
        print('{:6}|{:5}'.format(x,y))
        if y == menor:
            num_menor = (f'O menor número digitado foi {y}, no índice {x}...')
        if y == maior:
            num_maior = (f'O maior número digitado foi {y}, no índice {x}...')
        
    print(num_menor)
    print(num_maior)

# EXECUÇÃO DA FUNÇÃO
maior_menor(num, qt_num)
