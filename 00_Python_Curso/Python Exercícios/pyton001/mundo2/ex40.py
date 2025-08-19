''' cRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL DE ACORDO COM A MÉDSIA ATINGIDA
MEDIA ABAIXO DE 5 REPROVADO

MEDIA ENTRE 5 E 6.9  RECUPERAÇÃO

MEDIA DE 7 A 10 APROVADO

'''

n1 = float(input('Nota de Matemática?'))

n2 = float(input('Nota de português'))

m = ((n1+n2)/2)

print ("a média é", m) 

if m < 5 :
    print('Você está Reprovado')

elif m > 5 and m < 7 :
    print('Recuperação')

elif (m > 6.9) and (m <= 10) :
    print('APROVADO!')