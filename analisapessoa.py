somaidade = 0
idade = 0
for p in range(1,5):
    print('============= {}ª Pessoa ==========='.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]:')).strip()
    somaidade += idade
print('Soma de idades: {}'.format(somaidade))


