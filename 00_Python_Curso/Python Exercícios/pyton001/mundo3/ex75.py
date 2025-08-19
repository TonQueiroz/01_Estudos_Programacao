#leia 4 valores e coloqueos em uma tupla.
#Quantas vezes apareceu o valor 9
#EM que posução está o valor 3
#Quais foram os números pares

from random import randint
''' MEU CODIGO
n1 = int(input('Digite o 1º Valor!'))
n2 = int(input('Digite o 2º Valor!'))
n3 = int(input('Digite o 3º Valor!'))
n4 = int(input('Digite o 4º Valor!'))

tupla=  (n1, n2, n3, n4)'''

#Código professor!
tupla = (int(input('Digite o 1º Valor!')),int(input('Digite o 2º Valor!')),int(input('Digite o 3º Valor!')),int(input('Digite o 4º Valor!')))

print ('-=' *30)
print(f' O número 9 apareceu {tupla.count(9)} vezes')
print ('-=' *30)

if 3 in tupla:
    print(f' O número 3 está na posição {tupla.index(3)+1}.')
else:
    print(f' O número 3 não aparece nessa tupla')

print ('-=' *30)

cont= 0
for c in range (len(tupla)):
    if tupla[c]%2 == 0 :
        print ('-- ', tupla[c], end=" --  " )
        cont += 1



    
if cont == 0 :
    print('não temos números pares.') 
else:
    print ('São os Números pares')   

print ('-=' *30)




    
