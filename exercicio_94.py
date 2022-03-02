# exercicio 94
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo [m/f]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('quer continuar? [s/n] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N.')
    if resp == 'N':
        break
print(f' A) ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f' B) a media das idades é de {media:5.2f} anos.')
print(' C) as mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(' D) lista das pessoas que estão acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
