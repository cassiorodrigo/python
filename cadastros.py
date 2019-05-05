from datetime import date
count = 0
male = 0
female = 0
ano = date.today().year
maiores = 0
mmaiordeXanos = 0
while True:
    count += 1
    nome = str(input('Digite o Nome: '))
    nascimento = int(input(f'Digite o ano de nascimento de {nome}: '))
    sexo = str(input(f'Escolha o sexo de {nome} [M/F]: ')).strip().lower()[0]
    idade = ano - nascimento
    if sexo not in 'mf':
        sexo = str(input(f'Escolha o sexo de {nome} [M/F]: ')).strip().lower()[0]
    if sexo == 'm':
        male += 1
    if sexo == 'f':
        female += 1
    if idade > 18:
        maiores += 1
    if sexo == 'f':
        if idade > 20:
            mmaiordeXanos += 1
    c = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if c not in 'sn':
        c = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if c in 'Nn':
            break
print(f'Total de {count} pessoas cadastradas com sucesso.')
print(f'Dessas, {maiores} pessoas são maiores de 18 anos.')
print(f'Foram cadastrados {male} homens.')
print(f'Foram cadastradas {mmaiordeXanos} mulheres com mais de 20 anos.')
