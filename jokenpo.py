from time import sleep
from random import randint
com = randint(1, 3)
#if com == 1
escolha = int(input(" Para \033[31m Pedra \033[m digite 1\n Para \033[31m Papel \033[m digite 2\n Para \033[31m Tesora \033[m digite 3\n"))
sleep(0.5)
print('\033[32m JO \033[m')
sleep(0.5)
print('\033[32m KEN \033[m')
sleep(0.5)
print('\033[32m PO \033[m')
if escolha == 1 and com == 1:
    print('Você escolheu Pedra e eu também! É um empate!!!')
elif escolha == 2 and com ==1:
    print('Você escolheu Papel e eu escolhi Pedra. Você ganhou! :(')
elif escolha == 3 and com ==1:
    print('Você escolheu tesora. Pedra quebra tesoura. Eu ganhei!!! :)')
elif escolha == 1 and com == 2:
    print('Papel envolve Pedra. Eu ganhei!!! :)')
elif escolha == 2 and com == 2:
    print('Os dois Escolheram papel. É um empate!!!')
elif escolha == 3 and com ==2:
    print('Tesora corta Papel. Você ganhou')
elif escolha == 1 and com == 3:
    print('Pedra quebra tesora. Você ganhou!!!')
elif escolha == 2 and com == 3:
    print('Tesora corta papel. Eu ganhei!!!')
else:
    print('Duas tesoras. Deu empate!!!')
1