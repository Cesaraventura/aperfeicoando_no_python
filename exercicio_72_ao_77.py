# ex 72
cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze','doze', 'treze',
        'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('tente novamente. ', end='')
print(f'voce digitou o numero {cont[num]}')

# ex 73
times = ('atletico-mg', 'flamengo', 'palmeiras', 'fortaleza', 'corinthians', 'bragantino', 'fluminense', 'america-mg',
        'atlético-go', 'santos', 'ceara', 'internacional', 'são paulo', 'athletico', 'cuiaba', 'juventude', 'gremio',
        'bahia', 'sport', 'chapecoense')
print(f'lista de times do brasileirao: {times}')
print(f'os cinco primeiros são: {times[0:5]}')
print(f'os quatro ultimos são: {times[-4:]}')
print(f'times em ordem alfabética: {sorted(times)}')
print(f'o chapecoense esta na {times.index("chapecoense")+1}a posição')

# ex 74
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\no maior numero sorteado foi {max(numeros)}')
print(f'o menor numero sorteado foi {min(numeros)}')

# ex 75
num = (int(input('digite um numero: ')),
       int(input('digite outro numero: ')),
       int(input('digite mais um numero: ')),
       int(input('digite o ultimo numero: ')))
print(f'voce digitou os valores: {num}')
print(f'o valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'o valor 3 apareceu na {num.index(3)+1} posição.')
else:
    print('o valor 3 não foi digitado.')
print('os valores pares digitados foram:', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

# ex 76
listagem = ('lapis', 1.75,
            'borracha', 2,
            'caderno', 15.90,
            'estojo', 25)
print('-' * 38)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')

# ex 77
palavras = ('aprender', 'programar', 'linguagem')
for p in palavras:
    print(f'\nna palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
