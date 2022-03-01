# exercicio 93
jogador = dict()
partidas = list()
jogador['nome'] = str(input('nome do jogador: '))
tot = int(input(f'quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]    #recebendo uma cópia
jogador['total'] = sum(partidas)     #recebe a soma das partidas
print(jogador)

for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f'    => na partida {i}, fez {v} gols.')
print(f'foi um total de {jogador["total"]} gols.')

# 3 maneiras de fazer