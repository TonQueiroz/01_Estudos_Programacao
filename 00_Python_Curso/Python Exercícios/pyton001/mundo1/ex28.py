'''Escreva um programna que faça o computador escolher 
um número de 0 a 5 e pela para o usuário acertar o número escolhido
 pelo computador e escrever se o usuário perdeu ou foi derrotado pela maquina!'''

'''import random

npc = random.randint(0,5)

nus = int(input('acerte o número de 0 a 5 escolhido pelo computador...').strip())

if nus == npc:
    print(f' PArabéns vc cagou e acertou! o úmero escolhido pelo PC é - {npc}')

else:
    print(f' você está sem sorte! O número escolhido pelo PC Foi - {npc}')

print('--FIM DE JOGO--')'''


# Programa professor

from  random import randint

from time import sleep

computador = randint(0,20)

print ('-=-' *20)

print( f'Vou pensar em um número entre 1 e {20}, tente acertar....')

print('-=-'*20)

jogador = int(input('Em que número pensei?'))

sleep (3) #Comando para segurar por 3 segundos paran executar a proxima linha


if computador == jogador:

    print('Aeeee!!! Você ganhooouuu!')

else :
    print(f'EROOOU! Pensei no número {computador}, e não no número {jogador}.')
