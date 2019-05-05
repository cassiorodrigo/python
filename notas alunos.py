fin = list()
sec = list()
nome = list()
notas = list()
nome1 = ''
nota1 = nota = media = 0
while True:
    nome1 = str(input('Nome do Aluno: '))
    nome.append(nome1)
    nota = float(input('Primeira Nota do Aluno: '))
    while nota > 10 or nota < 0:
        print('Valor inválido. Notas devem variar de 0 a 10 com uma casa decimal.')
        nota = float(input('Primeira Nota do Aluno: '))
    nota1 = float(input('Segunda nota do Aluno: '))
    while nota1 > 10 or nota1 < 0:
        print('Valor inválido. Notas devem variar de 0 a 10 com uma casa decimal.')
        nota = float(input('Primeira Nota do Aluno: '))
    media = (nota + nota1) / 2
    notas.append(nota)
    notas.append(nota1)
    notas.append(media)
    sec.append(nome[:])
    sec.append(notas[:])
    fin.append(sec[:])
    nome.clear()
    notas.clear()
    sec.clear()
    resp = str(input('Deseja continuar? [S/N]'))
    if resp not in 'SsNn':
        print('Entrada Inválida. Digite "S" para "Sim" ou "N" para "não".')
        resp = str(input('Deseja Continuar? [S/N]'))
    if resp in 'Nn':
        break
aluno = list(enumerate(fin))
count = 0
for e in aluno:
    print(f' Para ver os dados de {aluno[count][1][0][0]} digite {aluno[count][0]}')
    count += 1
while True:
    select = int(input('\nDeseja ver os dados de qual aluno (Digite 999 para parar)? '))
    if select > len(fin) - 1 and select != 999:
        print('\nEntrada Inválida, por favor, digite o número correspondente a um aluno.')
    if select == 999:
        break
    if select < len(fin):
        print('-=' * 40)
        print(f'''
        O desempenho do aluno {aluno[select][1][0][0]} foi:
        Primeira nota: {aluno[select][1][1][0]}
        Segunda nota: {aluno[select][1][1][1]}
        Média foi: {aluno[select][1][1][2]}
        ''')
        count += 1
        print('-='*40)
