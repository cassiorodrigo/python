pessoas = list()
dados = list()
mai = men = 0
count = 0
while True:
    a = str(input('Nome: '))
    b = int(input('Idade: '))
    dados.append(a)
    dados.append(b)
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continua = str(input('Deseja continuar? [S/N]'))
    if continua in 'Nn':
        break
print(f'Foram {len(pessoas)} pessoas cadastradas.')
print(f'O maior peso cadastrado foi {mai}kg')
for p in pessoas:
    if p[1] == mai:
        print(p[0])
print(f'O menor peso cadastrado foi {men}kg')
for p in pessoas:
    if p[1] == men:
        print(p[0])
