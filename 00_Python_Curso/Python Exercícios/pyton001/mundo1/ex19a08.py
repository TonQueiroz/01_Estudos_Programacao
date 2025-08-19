#Sorteando um aluno para apagar a lousa

import random

alunos = [] #Lista em branco

print('Selecione 4 alunos')

alunos.append(input("1º")) #Adicionando itens na Lista em branco
alunos.append(input("2º"))
alunos.append(input("3º"))
alunos.append(input("4º"))

print(alunos)

escolhadealuno = random.choice(alunos)

print('O aluno escolhido foi: \n {}'.format(escolhadealuno))