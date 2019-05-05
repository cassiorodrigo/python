from random import randint
com = randint(0, 10)
count = 0
user = 11
while com != user:
    count += 1
    user = int(input('Digite seu palpite: '))
    if user > com:
        print('Seu chute foi muito alto! Tente um número menor,')
    elif user < com:
        print('Seu chute foi muito baixo. Tente um número maior')
print('Você acertou!!! Você precisou de {} tentativas para acertar.'.format(count))
