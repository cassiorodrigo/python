from random import randint
while True:
    opt = str(input('Você quer par ou ímpar? [P/I] \n')).lower().strip()
    if opt not in 'pi':
        print('Digite uma opção válida!')
    else:
        jogador = int(input('Digite um número para jogar: '))
        computador = randint(1, 3)
        if opt == 'p':
            if (jogador + computador) % 2 != 0:
                print(f'Eu escolhi {computador}. Você perdeu! Deu ímpar!')
                break
            else:
                print(f' Eu escolhi {computador}. Deu Par. Você ganhou!')
        if opt == 'i':
            if (jogador + computador) % 2 == 0:
                print(f'Eu escolhi {computador}. Você perdeu! Deu par!')
                break
            else:
                print(f'Eu escolhi {computador}.Você ganhou! Deu ímpar!')