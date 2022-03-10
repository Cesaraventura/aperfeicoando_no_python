# ex 98
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'contagem de {i} ate {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

#PROGRAMA
contador(1, 10, 1)
contador(10, 0, 2)
print('agora é sua vez de personalizar a contagem!')
ini = int(input('inicio: '))
fim = int(input('fim: '))
pas = int(input('passo: '))
contador(ini, fim, pas)
