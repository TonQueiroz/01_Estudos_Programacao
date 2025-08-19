'''SOMA DE TODOOS SO NUMEROS IMPARES QUE SÃO DIVISIVEIS POR E 3 NO INTERVALO DE 1 A 500'''

start = int(input('''SOMA DE TODOOS SO NUMEROS IMPARES QUE SÃO DIVISIVEIS POR E 3 NO INTERVALO DE 1 A 500 
                  [1] start'''))

soma = 0

# o meu em '''
'''
for c in range(1,500):
    if c%2 == 1:
        if c%3 == 0:
            soma += c

print (soma)'''

# O do  Professor pulando de 2 em 2 no laço o contador acessa menos o processador otimizando o assim o programa diminuindo o número de iterações.

for c in range(1,501, 2 ):
        if c%3 == 0:
            soma += c

print (soma)

        


