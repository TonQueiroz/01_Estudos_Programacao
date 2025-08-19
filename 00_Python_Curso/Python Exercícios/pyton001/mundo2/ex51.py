'''DESENVBOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PROGRESSÃO ARITIMÉTICA NO FINAL MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO'''
pt = int(input('Digite o primeiro termo da progressão aritimética \n'))
rp = int(input('Digita a razão da progressão aritimética\n'))

print('\33[31m')

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

soma = pt

for c in range (1,10+1):
    print(soma)
    soma += rp

