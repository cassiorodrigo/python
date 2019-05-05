par = list()
imp = list()
tot = list()
num = 0
count = 0
for c in range(0, 7):
    count += 1
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        imp.append(num)
par.sort()
imp.sort()
tot.append(par)
tot.append(imp)
print('-='*30)
print(f'''O total de números digitados foi {count}, sendo que:
Os números pares foram: {tot[0]}
e
Os números ímpares foram: {tot[1]}''')
print('-='*30)
