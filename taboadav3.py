n = count = m = 0

while True:
    count += 1
    n = int(input('Quer ver a taboada de qual valor?'))
    if n < 0:
        break
    while m < 10:
        m += 1
        taboada = n * m
        print(f'{n} x {m} = {taboada}')
    m = 0
