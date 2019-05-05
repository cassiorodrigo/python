print('='*40)
print(f'{"Lista de preços":^40}')
print('='*40)

produtos = ('lapis', 3,
            'caneta', 5,
            'borracha', 0.5,)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='')
    if c % 2 != 0:
        print(f'R${produtos[c]:>.2f}')