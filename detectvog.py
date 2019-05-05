vogais = ('a', 'e', 'i', 'o', 'u')
word = str(input('''Digite uma palavra para ver as suas vogais.
Digite espaço para encerrar: ''')).lower()
count = 0
while word != ' ':
    for letra in word:
        if letra in 'aeiou':
            print(f'{letra}')
            count += 1
    print(f'Foram {count} vogais detectadas')
    count = 0

    word = str(input('Digite outra palavra: '))
#        elif vogais[count] not in word:
#                print('Nenhuma vogal foi detectada!')

