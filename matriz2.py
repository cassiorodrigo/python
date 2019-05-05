linha1 = list()
linha2 = list()
linha3 = list()
matriz = list()
somapar = 0
soma3co = 0
num = 0
count = 0
linha = coluna = 0
for c in range(0, 9):
    num = int(input(f'Diginte um número para a posição {linha, coluna}: '))
    if c < 3:
        linha1.append(num)
    elif 2 < c < 6:
        linha2.append(num)
    elif 5 < c < 10:
        linha3.append(num)
    coluna += 1
    if coluna == 3:
        coluna = 0
        linha += 1
matriz.append(linha1)
matriz.append(linha2)
matriz.append(linha3)
print(f'''
    [  {matriz[0][0]}  ] [  {matriz[0][1]}  ] [  {matriz[0][2]}  ]

    [  {matriz[1][0]}  ] [  {matriz[1][1]}  ] [  {matriz[1][2]}  ]

    [  {matriz[2][0]}  ] [  {matriz[2][1]}  ] [  {matriz[2][2]}  ]            

''')
print(matriz)
for p in matriz:
    if p[0] % 2 == 0:
        somapar += p[0]
    if p[1] % 2 == 0:
        somapar += p[1]
    if p[2] % 2 == 0:
        somapar += p[2]
print(f'O valor da soma de todos os números pares é: {somapar}')
soma3co = (matriz[0][2] + matriz[1][2] + matriz[2][2])
print(f'A soma dos valores da 3ª Coluna é: {soma3co}')
if matriz[1][0] > matriz[1][1] and matriz[1][0] > matriz[1][2]:
    print(f'O maior valor da segunda linha é: {matriz[1][0]}')
if matriz[1][1] > matriz[1][0] and matriz[1][1] > matriz[1][2]:
    print(f'O maior valor da segunda linha é: {matriz[1][1]}')
if matriz[1][2] > matriz[1][0] and matriz[1][2] > matriz[1][1]:
    print(f'O maior valor da segunda linha é: {matriz[1][2]}')