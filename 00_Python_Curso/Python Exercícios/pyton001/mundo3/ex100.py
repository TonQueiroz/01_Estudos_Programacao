# Lista numeros com 2 funções uma função sorteia e outra chamada soma par 
# Sorteia Adiciona 5 numeros aleatórios a lista
#SomaPar vai mostrar a soma entre todos os valores pares sorteados na função anterior

from random import randint
from time import sleep
numeros = []
def pares(n):
    s = 0
    for i in n:
        if i%2==0:
            s += i
    sleep(2)
    print(f'As somas dos números pares foram -')
    sleep(2)
    print(f'{s}', flush=True)
    
def sorteia(lista):

    for c in range (0,5):
        lista.append(randint(0,100))
    print (f'Os números sorteados foram -')
    sleep(2)
    print (f'{lista}', flush=True)

print ('-='*30)
sorteia(numeros)
print ('-='*30)
pares(numeros)
print ('-='*30)




    
    



