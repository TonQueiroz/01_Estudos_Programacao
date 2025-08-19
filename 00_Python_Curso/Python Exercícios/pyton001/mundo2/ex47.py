'''quais os númeroos pares de 1 a 50'''

start = int(input('Quer saber os números de pares OU IMPARES ENTRE 1 E QUALQUER OUTRO NÚMERO? [1] PARES [2] IMPARES'))

n = int(input('qual número ?'))

'''if start == 1:
    for c in range (1,n+1):
        print('.', end=" ")
        if c % 2 == 0:
            print(c, end=" ")

    print('pronto estÃO aí')

elif start == 2:
    for c  in range(1,n+1):
        if c%2 == 1:
            print(c, end=" ")

else:
    print('ENTRADA INFVALIDA')

print('ACABOU')'''

# diminuindo o número de iterações (vezes que o programa solicita seu processador) no processador para otimizar o programa

if start == 1:
    for c in range (2,n+1, 2):
        print('.', end=" ")
        print(c, end=" ")

if start == 2:
    for c in range (1,n+1, 2):
        print('.', end=" ")
        print(c, end=" ")

print('ACABOU')
        