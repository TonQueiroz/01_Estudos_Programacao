#Tabuada de varios número umd e cada vez E pare quando o número solicitado for negativo

from random import randint

c = 0

while True:
    jogadorp = " "
    while jogadorp not in "PI":
        jogadorp = str(input('Par ou Impar?')).upper().strip()[0]

    jogadorn = int(input('Qual o número?'))

    computador =  randint(1,10)

    if (jogadorn + computador)%2==0:
        resultado = 0
        R = 'DEU PAR!'

        c += 1 
    else:
        resultado = 1
        R = 'DEU IMPAR!'

    if resultado == 0 and jogadorp == 'P' or resultado == 1 and jogadorp == 'I':
        print(f' VOCÊ {jogadorn} - COMPUTADOR {computador} = {R} \n Parabéns Jogador! Você ganhou! Jogue nomavemte!')

    else:
        print(F'VOCÊ {jogadorn} - COMPUTADOR {computador} = {R}!! \nVOCÊ PERDEU! O JOGO ACABA AQUI PRA VOCÊ!')
        break

           
print (f'Você teve {c} Vitórias consecutivas!')


    

    
