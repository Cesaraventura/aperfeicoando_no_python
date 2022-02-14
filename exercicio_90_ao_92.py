# ex 90
aluno = dict()
aluno['nome'] = str(input('nome: '))
aluno['media'] = float(input(f'media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'recuperacao'
else:
    aluno['situacao'] = 'reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')

# ex 91
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f' - {i+1}o lugar: {v[0]} com {v[1]}')
    sleep(1)

# ex 92
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['carteira de trabalho'] = int(input('carteira de trabalho (0 para nao tem e 1 para tem): '))
if dados['carteira de trabalho'] != 0:
    dados['contratacao'] = int(input('ano de contratacao: '))
    dados['salario'] = float(input('salario: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f'   - {k} tem o valor de {v}')
