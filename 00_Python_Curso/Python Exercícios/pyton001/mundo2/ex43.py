''' EXERCÍCIO 43 --- DESENVOLVA UMA LOGICA QUE LEIA O 
PESO E A ALTURA CALCULE SEU IMC E MOSTRE SEU STATUS DE ACORDO COM A TABELA ABAIXO


<18 ABAIXO DO PESO

ENTRE 18 E 25 pESO IDEAL

ENTRE 25 E 30  - SOBREPESO

ENTRE 30 E 40 OBESO

ACIMA DE 40 OBESIDADE MORBIDA'''


peso = float(input('QUAL SEU PESO?'))

altura = float(input('QUAL SUA ALTURA?'))

IMC = peso /(altura**2)

if IMC < 18:
    print ('VOCÊ ESTÁ ABAIXO DO PESO IDEAL')
elif IMC >= 18 and IMC < 25 :
    print ('VOCE ESTÁ NO PESO IDEAL')
elif IMC >= 25 and IMC < 30 :
    print ('VOCE ESTÁ NO SOBREPESO')
elif IMC >= 25 and IMC < 30 :
    print ('VOCE ESTÁ NO OBESO')
elif IMC >= 30 and IMC < 40 :
    print ('VOCE ESTÁ NO SOBREPESO')
elif IMC >= 40:
    print ('VOCE ESTÁ EM OBESIDADE MÓRBIDA ')

print(f' Seu imc é {IMC}')