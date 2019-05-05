from random import randint
elements = int(input('how many elements do you want to generate? \n'))
contador = 0
listaa = list()
listab = list()
listac = list()
while contador < elements:
    contador += 1
    num = randint(0, 10)
    listaa.append(num)
contador = 0
elements = int(input('how many elements do you want to generate? \n'))
while contador < elements:
    contador += 1
    num = randint(0, 10)
    listab.append(num)

listac = listaa + listab
print(listaa)
print(listab)
print(listac)
for e in range(0, len(listac)):
    for i in listac:
        if listac.count(i) > 1:
            listac.remove(i)
listac.sort()
print(listac)
