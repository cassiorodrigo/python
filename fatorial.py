from math import factorial
fac = int(input('Digite um numero inteiro: '))
count = fac
f = 1
'''while count > 0:
    f *= count
    count -= 1
print(f)'''

for r in range(count + 1, 1, -1):
    if fac is int:
        print('Entrada errada. Por favor, digite uma enttrada válida')
    else:
        f *= count
        count -= 1
print('O fatorial é: {}! = {}'.format(fac, f))




