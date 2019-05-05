#!/usr/bin/python
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
palpite = ''
palpiteli = list()
advinha = ''
posicao = 0
count = 0
palavra = str(input('Digite a palavra a ser advinhada: ')).lower()
print('\n'*39)
palavrali = list(palavra)
print(f'A palavra chave tem {len(palavra)} caracteres')
espacos = ('_' * len(palavra))
palavratemp = list(espacos)
print(palavratemp)

while True:
    opcao = int(input ('''
	Digite [1] para chutar uma letra 
	ou
	Digite [2] para advinhar a palavra.
	opcao: '''))
    if opcao == 1:
        palpite = str(input('Digite uma letra: '))
        if len(palpite) == 0:
            palpite = str(input('Campo vazio. Digite uma letra: '))
        else:
            if palpite not in palavra:
                count += 1
                print(f'A palavra chave não contém {palpite}')
            if count == 6:
                print('Você perdeu. seu bonequinho foi desenhado na forca.')
                break
            if palpite in palavra:
                for i in range(0, palavra.count(palpite)):
                    palpiteli.append(palpite)
            for e in palavra:
                if e != palpite:
                    palavrali[palavrali.index(e)] = '_'
                    palavratemp = palavrali[:]
            print(palavratemp)
            palavrali = list(palavra)                 
            print(palpiteli)
        if len(palpiteli) == len(list(palavra)):
            print(f'A palavra chave era:"{palavra}". Você acertou todas as letras!!!') 
            break
    if opcao == 2:
        advinha = str(input('Qual é a palavra chave? \nDigite seu palpite: \n'))
        if list(palavratemp) == list(palavra):
            print(f'A palavra chave era:"{palavra}". Você acertou todas as letras!!!')
        else:
            print('Você perdeu!')
        break           