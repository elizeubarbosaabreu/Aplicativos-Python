# Este prrograma calcula descontos
# Elizeu Barbosa Abreu
novo = True
while novo == True:
    print('{:.^50}'.format('CALCULADORA DE DESCONTOS'))
    print('{:.>50}'.format('OBS.: Use "." no lugar de ",". EX.: R$40.25'))
    valor_do_produto = float(input('\nValor do produto : R$'))
    desconto = float(input('Porcentagem de desconto: %'))
    valor_desconto = valor_do_produto*(desconto/100)
    total_pagar = (valor_do_produto-valor_desconto)
    print('{:.^40}'.format(''))
    print('O produto custava: R${:2.2f}\nDesconto: {:2.0f}%\nDesconto em dinheiro: R${:2.2f}\nValor a Pagar: R${:2.2f}'.format(valor_do_produto, desconto,valor_desconto,total_pagar))
    print('{:.^40}'.format(''))
    c = input('Deseja realizar novo Calculo:\nS para Sim | N para Não : ')
    if c == 's' or c == 'S':
        print('{:.^40}'.format(''))
        novo = True
    else:
        print('{:.>50}'.format('Bye Bye'))
        print('{:.>50}'.format('OK?'))
        novo = False
    
