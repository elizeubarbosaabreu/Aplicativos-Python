a = [] # Cria uma lista vazia

# append(x) adiciona o item x na lista
while True: # Enquanto verdadeiro sempre coletar item na lista
    new = str(input('Entre com um elemento na lista: '))
    if new in a:
        print(f'Item "{new}" já existe... \nNão foi possível Adicionar!')
        pass
    else:
        a.append(new)
        print(f'Item "{new}" adicionado!')
    
    c = input('Desejas continuar? (S/N):').upper()[0] #[0] Pega apenas a primeira letra [s]im
    
    if c == 'S':
        continue
    else:
        break
    
print(f'Os elementos da lista A são: {a}')

# pop() apaga o último item da lista
print(f'O comando abaixo vai apagar o item "{a[-1]}"')
ok = input('tudo bem? (s/n)').upper()[0]
itemApagado = a[-1]
if ok == 'S':
    a.pop()
    print(f'Item {itemApagado} deletado com sucesso...')
else:
    print(f'Tudo bem não apaguei nada!')
print(a)

# remove('x'), busca e remove o item 'x' da lista
aremover = input('Que item deseja remover: ')
if aremover in a:
    a.remove(aremover)
    print(f'Removi o item "{aremover}".')
else:
    print(f'Não encontrei "{aremover}".')    
print(a)

b = a[:] # b recebe cópia de a completamente sem vinculação

b[0] = '@elizeu.barbosa.abreu' #adiciona '@elizeu.barbosa.abreu' no índice 0 da lista b
print(f'a = {a}')
print(f'b = {b}')
