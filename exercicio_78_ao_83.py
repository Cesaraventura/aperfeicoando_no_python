# ex 78
listanum = []
maior = 0
menor = 0
for c in range(0,5):
    listanum.append(int(input(f'digite um numero para a posicao {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print(f'voce digitou os valores {listanum}')
print(f'o maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):    #i = indice, v = valor
    if v == maior:
        print(f'{i}...', end='')
print()    #print pra quebra de linha
print(f'o menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()

# ex 79
numeros = list()
while True:
    n = int(input('digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('valor adicionado com sucesso.')
    else:
        print('valor ja existente. adicione outro valor.')
    r = str(input('quer continuar? [s/n] '))
    if r in 'Nn':
        break
numeros.sort()    #colocar em ordem crescente
print(f'voce digitou os valores {numeros}.')

# ex 80
lista = []
for c in range (0,5):
    n = int(input('digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'adicionado na posição {pos} da lista.')
                break
            pos += 1
print(f'os valores digitados em ordem foram {lista}.')

# ex 81
valores = []
while True:
    valores.append(int(input('digite um valor: ')))
    resp = str(input('quer continuar? [s/n] '))
    if resp in 'Nn':
        break
print(f'voce digitou {len(valores)} valores.')
valores.sort(reverse=True)      #reverse=true é quando eu quero algo na ordem decrescente
print(f'os valores em ordem decrescente são {valores}.')
if 5 in valores:
    print('o valor 5 faz parte da lista!')
else:
    print('o valor 5 nao faz parte da lista!')

# ex 82
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('digite um numero: ')))
    resp = str(input('quer continuar? [s/n] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'a lista completa é {num}')
print(f'numeros pares {pares}')
print(f'numeros impares {impares}')

# ex 83
expr = str(input('digite sua expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()         #o .pop deleta um valor da pilha
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expressao esta valida.')
else:
    print('sua expressao nao esta valida.')
