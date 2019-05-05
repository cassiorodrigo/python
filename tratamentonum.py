
count = 0
soma = 0
n = int(input('Digite um numero: '))
while n != 999:
    count += 1
    soma += n
    n = int(input('Digite um numero: '))
print('Você digitou {} numeros e a soma entre eles é {}'. format(count, soma))