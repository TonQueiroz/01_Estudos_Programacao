#Gere 5 numeros aleatórios coloqueos em uma tupla.
#mostre a listagem dos numeros gerados o menos e o maior valor

from random import randint

n1 = randint(0,100)
n2 = randint(0,100)
n3 = randint(0,100)
n4 = randint(0,100)
n5 = randint(0,100)


tupla = (n1, n2, n3 , n4, n5 )

nmen = 0
nmai = 0

for c in range (len(tupla)):
    

    if  tupla[c] < nmen  or  c == 0:
        nmen = tupla[c]
    
    if  tupla[c] > nmai  or  c == 0:
        nmai = tupla[c]
    
    


print ('-=' *30)

print (' A tupla completa é Tupla é\n ',tupla)

print ('-=' *30)

print(' O menor número da Tupla é\n ',nmen)

print ('-=' *30)
print(' O maior número da Tupla é\n ', nmai)

print ('-=' *30)

#--------------------------EXERCÍCIO PROFESSOR--------------------------#

print( '-=' *30,'EXERCÍCIO PROFESSOR', '-=' *30)

tp = (randint(0,100),randint(0,100),randint(0,100),randint(0,100))


print(f' Os números sorteados foram \n {tp}')

print(f'O maior número foi \n {max(tp)}')

print(f'O menor número foi \n {min(tp)}')