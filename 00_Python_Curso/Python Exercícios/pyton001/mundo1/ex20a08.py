#Sorteando os alunos para ordem de apresentação

import random

alunos = ['Pedro', 'João', 'Maria', 'ana'] #Lista em branco

print('Selecione 4 alunos')

'''alunos.append(input("1º")) #Adicionando itens na Lista em branco
alunos.append(input("2º"))
alunos.append(input("3º"))
alunos.append(input("4º"))
'''
print(alunos)

escolhadealuno = random.sample(alunos, 2)

embaralhamento = random.sample(alunos, len(alunos))


print('Os 2 alunos escolhidos com sample foram: \n {}'.format(escolhadealuno))

print('lista embaralhada \n {}'.format(embaralhamento))