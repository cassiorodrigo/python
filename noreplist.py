palavras = [1, 'amor', 2, 'amor', 1, 'amor', 2, 'amor', 1, 'amor']
print(palavras.count('amor'))
for e in range(0, len(palavras)):
    for i in palavras:
        if palavras.count(i) > 1:
            palavras.remove(i)


