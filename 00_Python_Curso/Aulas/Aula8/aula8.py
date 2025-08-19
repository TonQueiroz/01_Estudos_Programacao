import math

n= int(input('Escolha um Número?'))

raiz = math.sqrt(n) #Se importar a bibliotteca toda é preciso colocar o math. 
                        #antes da função desejada para se referir a biblioteca e escolher a função nela

print('Essa é a Raiz quadrada de {} por sem import = {}'.format(n, n**0.5))

print('Essa é a Raiz quadrada de {} por com import da biblioteca Math = {}'.format(n, raiz))

#------------------------------------

from math import sqrt

n= int(input('Escolha um Número?'))

raiz = sqrt(n) #quando importar a função específica dentro da biblioteca não é preciso colocar o math. 
                #antes da função desejada pois vc importou direto a função e não a biblioteca

print('Essa é a Raiz quadrada de {} por sem import = {}'.format(n, n**0.5))

print('Essa é a Raiz quadrada de {} por com import da biblioteca Math = {}'.format(n, raiz))

#As bibliotecas são consultadas no site oficial do Pyton Comunity

import random #biblioteca Random

num1 = random.random() # Busca um numero aleatorio entre 0 e 1 

num3 = random.randint(1,100) # Busca um numero aleatorio INTEIRO entre 1 e 10 

print (num1)

print (num3)

import emoji #Para adicionar bibliotecas novas não preinstaladas no python buscar no PYPI no site oficial e copiar o código da 
            # biblioteca desejada colar no terminal e será feita a instalação e os emojis vc ve em Emoji Cheat Sheet mp sitte

print(emoji.emojize("Python é :polegar_para_cima:", language='pt'))