from time import sleep

select1 = selec = 0
print('=' * 50)
print('\n')
print('{:^50}'.format('BEM VINDO ao LIBERAPP'))
print('{:^50}'.format('O aplicativo que te ensina liberdade'))
print('\n')
print('=' * 50)

while True:
    selec = int(input('''
    Selecione um nível para testar o seu conhecimento sobre a liberdade: 
    Digite [ 1 ] para nível "Curioso" (somente selecione este nível se você é novo na idéia de liberdade)
    Digite [ 2 ] para Nível Básico (Você já viu o básico de liberdade, mas ainda não consegue entender como as coisas funcionariam)
    Digite [ 3 ] para nível Médio (Você já entende bem liberdade e quer aprofundar seu conhecimento)
    Digite [ 4 ] para Nível Avançado (Você está pensando: "Eu tinha que bater um papo com o desenvolver desse App!"
    
    selecione uma das opções: '''))
    if selec != 999:
        while selec > 4 or 1 > selec:
            print('\nOpção inválida, Tente novamente')
            selec = int(input('''
                   Selecione um nível para testar o seu conhecimento sobre a liberdade: 
                   Digite [ 1 ] para nível "Curioso" (somente selecione este nível se você é novo na idéia de liberdade)
                   Digite [ 2 ] para Nível Básico (Você já viu o básico de liberdade, mas ainda não consegue entender como as coisas funcionariam)
                   Digite [ 3 ] para nível Médio (Você já entende bem liberdade e quer aprofundar seu conhecimento)
                   Digite [ 4 ] para Nível Avançado (Você está pensando: "Eu tinha que bater um papo com o desenvolver desse App!"
    
                   selecione uma das opções: '''))
            if selec == 999:
                break
        else:
            print(f'Opção selecionada: {selec}. Carregando o módulo correspondente...')
            sleep(1)
            if selec == 1:
                print('Bem Vindo ao módulo "Curioso".')
                print('-' * 40)
                print('\nAqui você vai encontrar somente as bases filosóficas e éticas da liberdade\n')
                print('-' * 40)
                while select1 != 999:
                    select1 = int(input('''
                    Selecione um dos tópicos para saber mais:
                    [ 1 ] "Mas quem vai construir as Estradas?"
                    [ 2 ] "Coitados dos pobres. O que seria deles, sem o Estado?"
                    [ 3 ] "Sem Estado, quem vai cuidar da saúde?"
                    [ 4 ] "Sem polícia e sem leis coercitivas, iria virar bang bang, velho-oeste mesmo..."
                    seleção: '''))
                    if 1 > select1 > 4:
                        print('Opção inválida, Tente novamente')
                    if select1 == 1:
                        print('''
                        \nO Estado raramente constrói as estradas. Quando o faz, são mais custosas que o planejado e menos eficientes.
                         O que acontece na maioria das vezes é que o Estado é um mero intermediário entre as pessoas que estão "comprando" a estrada e os empreiteiros.
                         Como todos sabemos, eliminando o "intermediário" o projeto fica (bem) mais barato e do jeitinho que o cliente queria.
                         
                         Além disso, o Estado proíbe a competição, limitando o número de estradas que podem ser construídas. 
                         Se não há competição, o pedágio é, em regra, mais caro. 
                         
                         Por fim, houveram casos de estradas privadas construídas, que "cobravam" um pedágio opcional.
                          Um caso notório foi de um inglês que abriu um único caminho para uma vila, que estava isolada após um deslize de terras. 
                          Infelizmente, o Estado fechou a estrada por falta de "Alvará, condenando a vila à escassez de mantimentos até a reabertura
                          da via Estatal.\n''')
                    if selec == 2:
                        print(''' texto sobre os pobres''')
                    if selec == 3:
                        print(''' texto sobre a saúde''')
                    if selec == 4:
                        print('''texto sobre a segurança''')

            if selec == 2:
                print('''Bem Vindo ao módulo Básico.
                
                Aqui você vai encontrar um mini jogo de "perguntas e respostas" comentado''')

                select2 = str(input('Digite [S] para continuar: '))
                while select2 not in 'Ss':
                    select2 = str(input('Entrada Inválida. Aperte "S" para contunar: '))

            if selec == 3:
                print(
                    'Bem vindo ao módulo "Intermediário". \nAqui você vai encontrar propostas libertárias genéricas para resolução de problemas em uma sociedade livre')

            if selec == 4:
                print(
                    'Bem vindo ao módulo "Avançado". \nAqui você vai encontrar dicas de leitura, podcasts e vídeos sobre a liberdade. \nVocê também pode encontrar meu contato, se achar que você deveria estar escrevendo esse programa. :-)')

            if selec == 999:
                break
    if selec == 999:
        break