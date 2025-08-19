''' EXERCÍCIO 45 ---

CRIE UM JOCKENPÔ QUE FAÇA O COMPUTADOR JOGAR COM VOCÊ.
'''

from random import randint

from time import sleep


j1 =  int(input(f'  [1] Pedra, [2] papel ou [3]tesoura?'))

j2 = randint(1,3)

sleep (1)
print('JO')

sleep (1)
print('KEN')

sleep (1)
print('PO!!')


if j1 == 1 and j2 == 1:
    print (f''' EMPATE! 
           as tesouras se neutralizaram!!''')
    
elif j1 == 1 and j2 == 2:
    print (f''' PERDEU! 
           sua PEDRA foi embrulhada pelo PAPEL do computador!''')

elif j1 == 1 and j2  == 3:
    print (f''' GANHOU! 
           sua PEDRA amassou a TESOURA do computador!''')
    
elif j1 == 2 and j2 == 1 :
    print (f''' GANHOU! 
           sua PAPEL embrulhou a PEDRA do computador!''')
    
elif j1 == 2 and j2 == 2 :
    print (f''' EMPATE! 
           os PAPÉIS se neutralizaram!!''')
    
    
elif j1 == 2 and j2 == 3 :
    print (f''' PERDEU! 
           as A TESURA  do computador cortou seu PAPEL!!''')

elif j1 == 3 and j2 == 1 :
    print (f''' PERDEU!           
           sua TESOURA foi amassada pela PEDRA do computador!''')

elif j1 == 3 and j2 == 2 :
    print (f''' GANHOU!! 
           SUA TESOURA cortoou o papél do COMPUTADOR!''')
    
    
elif j1 == 3 and j2 == 3 :
    print (f''' EMPATE! 
           as TESOURAS se neutralizaram!!''')