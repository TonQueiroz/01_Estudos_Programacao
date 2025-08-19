'''LEIA A IDADE DE 7 PESSOAS E ME CONTE QUANTAS JÁ ATINGIRAM A MAIORIDADE'''


contador=0
for c in range (1,7+1):
    idade = int(input(f'Quantos anos a {c}ª pessoa tem ?'))
    if idade >=18:
        contador += 1

print (f'MAIORES DE IDADE ={contador}')

