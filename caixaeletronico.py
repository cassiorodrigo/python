cinq = dude = dez = unidade = rcinq = rdude = rdez = 0
saque = int(input('Qual o valor a ser sacado?\n'))

cinq = saque // 50
rcinq = saque % 50
dude = rcinq // 20
rdude = saque % 20
dez = rdude // 10
rdez = saque % 10
unidade = saque % 10
saque = cinq + dude + dez + unidade

print(f'Seu saque será composto de \n{cinq} notas de R$50,00 \n{dude} notas de R$20,00 \n{dez} notas de R$10,00  \n{unidade} notas de R$1,00')
