total = 0
count = 0
barato = 0
probarato = ''
procaro = ''
procarocount = 0
while True:
    count += 1
    produto = str(input('Digite o nome do produto: ')).strip().capitalize()
    preco = float(input('Digite o preço do produto'))
    total += preco
    if count == 1:
        barato = preco
    elif preco < barato:
        barato = preco
        probarato = produto
    if preco > 1000:
        procaro = produto
        procarocount +=1
    c = str(input('Deseja continuar/ [S/N]'))
    while c not in 'SsNn':
        c = str(input('Deseja continuar/ [S/N]'))
    if c not in 'Ss':
        break
print(f'''
O total da compra foi: {total:.2f}
O produto mais caro foi {procaro}
O produto mais barato foi {probarato} e custou {barato:.2f}
{procarocount} produtos custaram mais de R$1000,00''')