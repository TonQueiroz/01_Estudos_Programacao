#Hipotenusa de um triangulo retangulo a partir dos catetos com import de bibliotecas
import math

c1 = int(input('Tamanho do cateto 1? '))

c2= int(input('tamanho do cateto 2?'))

h= math.sqrt(((c1**2)+(c2**2))) #usando a função de raiz quadrada sqrt

himp = math.hypot(c1,c2) #usando direto a função de hipotenusa sqrt

print('A hipotenusa desse triangulo usando a função/funcionalidade de raiz quadrada é {}'.format(h))

print('A hipotenusa desse triangulo  com a função/funcionalidade de hipotenusa é {}'.format(himp))


#para pesquisar as funções das bibliotecas ir no site python.org e procurar em library references. 

