n = int(input('Quantos termos da sequencia de Fibbonacci você quer mostrar?\n'))
count = 3
t1 = 0
t2 = 1
print('{} -- {}'.format(t1, t2, end = ''))
while count <= n:
    count += 1
    t3 = t1 + t2
    print('{} -- '.format(t3, end = ''))
    t1 = t2
    t2 = t3
