''' A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENRTO DE UM ATLERA E MOSTRE SUA CATEGORIA DE ACORDO COM SUA IDADE

ATÉ 9 MIRIM

ATE 14 INFANTIL
ATE 19 JUNIO
ATE 20 SENIOR
MAIS QUE 20 MASTER

'''

idade = float(input("qual a sua IDADE?"))


print('Você está na Categotia')

if (idade <= 9) :
    print('MIRIM')

elif  (idade > 9) and (idade <=14): #'''(idade > 9) and <- NAO PRECISA DESSE PORQUE SE ELE CHEGOU NESSE ELIF ELE PASSOU PELO => 9 E A MESMA COISA NOS OUTROS!'''
    print('INFANTIL')

elif (idade>14) and (idade <= 19):
    print ('JUNIOR')

elif (idade>19) and (idade <= 35):
    print ('PROFISSIONAL') 

elif (idade>35):
    print ('SENIOR')

elif (idade>42):
    print ('MASTER')    