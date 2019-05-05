voto = 0
count = 0
espelho = list()
encerra = ''
while True:
    voto = int(input('Digite o número do seu candidato: '))
    if voto == 13:
        espelho.append(voto)
    if count % 2 == 0:
        voto = 13
        espelho.append(voto)
    else:
        espelho.append(voto)
    encerra = str(input('Deseja encerrar a votação? [S/N]'))
    count += 1
    if encerra in 'Ss':
        break

print(espelho)