linha1 = list()
linha2 = list()
linha3 = list()
matriz = list()
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
print(f'''
    [{linha1[0]}]       [{linha1[1]}]       [{linha1[2]}]
    
    [{linha2[0]}]       [{linha2[1]}]       [{linha2[2]}]
    
    [{linha3[0]}]       [{linha3[1]}]       [{linha3[2]}]            

''')
print(linha1, linha2, linha3)
