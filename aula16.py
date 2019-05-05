numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    num = int(input('Digite um numero entre 0 e 10: '))
    if num > 10:
        num = int(input('Entrada inválida. Tente novamente: Digite um valor entre 0 e 10'))
    if num < 0:
        num = int(input('Entrada inválida. Tente novamente: Digite um valor entre 0 e 10'))
    else:
        break
print(numeros[num])