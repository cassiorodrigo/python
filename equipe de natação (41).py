from time import sleep
from datetime import date
a = ('dd')
b = ('mm')
c = ('aaaa')
numero = str(input("Digite a data de nascimento no formato {}/{}/{}\n".format(a, b, c))).strip().rsplit()
ano = numero[0][6:] #separa o ano
if len(ano) != 4:
    print('Digite um ano Válido')
anodigitado = (ano.isnumeric())
if anodigitado is False:
    print('Digite um ano válido')

#print(ano) (VERIFICA SE O ANO FOI SEPARADO CORRETAMENTE)
ano2 = int(ano) #converte o ano digitado para int.
#print(type(ano2))
sleep(2)
atual = date.today().year
int(atual)
#print(date.today().year)

if atual - ano2 <= 9:
    print('Mirim')
elif atual - ano2 <= 14:
    print('Infantil')
elif atual - ano2 <= 19:
    print('Junior')
elif atual - ano2 <= 20:
    print('senior')
else:
    print('Master')
