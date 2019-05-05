num = count = soma = 0
while True:

    num = int(input(f'Digite um valor (999 para parar): '))
    if num == 999:
        break
    soma += num
    count += 1
print(f'A soma dos {count} numeros digitados é: {soma}')