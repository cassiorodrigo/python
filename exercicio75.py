pares = 0
a = int(input("Digite um número: "))
if a % 2 == 0:
    pares += 1
b = int(input("Digite um número: "))
if b % 2 == 0:
    pares += 1
c = int(input("Digite um número: "))
if c % 2 == 0:
    pares += 1
d = int(input("Digite um número: "))
if d % 2 == 0:
    pares += 1
seq = (a, b, c, d)
print(seq)
print(f'O numero 9 apareceu {seq.count(9)} vezes!')
if seq.count(3) != 0:
    print(f'O numero 3 foi digitado primeiro na posição {seq.index(3)+1}')
else:
    print(f'Nenhum numero 3 encontrado')
print(f'A quantidade de números pares digitados foi {pares}')
