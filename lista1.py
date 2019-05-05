valores = list()
count = 0

for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    resultados = list()
    resultados.append(max(valores))
    resultados.append(valores.index(max(valores)))
    resultados.append(min(valores))
    resultados.append(valores.index(min(valores)))
    for m in resultados:

print(resultados)

print(f'''
O maior valor digitado foi {resultados[0]}
A posição do menor valor digitado é {resultados[1]}
O menor valor digitado foi: {resultados[2]}
A posição do menor valor digitado é {resultados[3]}''')
