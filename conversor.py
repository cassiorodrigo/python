numero = int(input('Digite um Numero Inteiro\n'))
conversao = int(input('''Escolha uma das bases para conversão
[1] Converter para Binario
[2] Converter para Hexadecimal
[3] Converter para Octal'''))
if conversao == 1:
    print(bin(numero)[2:])
elif conversao == 2:
    print(hex(numero)[2:])
elif conversao == 3:
    print(oct(numero)[2:])
else:
    print('opção invalida')
