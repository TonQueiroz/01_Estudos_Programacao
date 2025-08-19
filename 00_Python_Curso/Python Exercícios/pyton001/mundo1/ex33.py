'''Maior numero e menor numero de 3'''

'''
n1 = int(input('1º?'))

n2 = int(input('2º?'))

n3 = int(input('3º?'))

if n1 > n2 and n1 > n3:

    nma = n1
    if n2 > n3:
        nme = n3
    else:
        nme = n2

elif n2 > n1 and n2 > n3:

    nma= n2
    if n1 > n3:
        nme = n3
    else:
        nme = n1

else: 
    nma = n3
    if n1 > n2:
        nme = n2
    else:
        nme = n1

print( f' O maior número é: {nma} \n O menor numero é {nme}')

'''

'''Opção do Professor ! HAHA''' #As vezes um desafio é muito mnais fácil do que parece.


a = int(input('1º'))
b = int(input('2º'))
c= int(input('3º'))

menor=a #Definindo o menor numero como a você elimina uma linha de códico para comparação e só compara o valor b e c.

if b<c and b < a:
    menor = b

if c<a and c<b:
    menor = c

print (f'o menor nº é {menor} ')

#definindo o maior

maior = a #Definindo o menor numero como a você elimina uma linha de códico para comparação e só compara o valor b e c.

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c


print(f'O maior nº é {maior}.')