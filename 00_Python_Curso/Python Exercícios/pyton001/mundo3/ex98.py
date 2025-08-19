# Função chamada CONTADOR  com 3 poarametros INÍCIO, FIM E PASSO 
# Realize a contagem atrtavés da funcção criada de 1 até 10 de 1 em 1
# De 10 até 0 de 2 em 2
# uma contagem personalizada

from time import sleep

def contagem (inicio,fim,passo):
    print('-='*20)
    if passo ==0:
        print('Passo foi alterado para 1')
        passo = 1
    elif inicio > fim and passo > 0:
        print('Seu passo alterado para negativo')
        passo= passo * -1

    elif inicio < fim and passo < 0: 
        print('Seu passo alterado para positivo')
        passo= passo * -1

    print (f'Contagem de {inicio} até {fim} a cada {passo} unidades.')    
        
    for c in range(inicio,fim,passo):
        
        print (c, end=" ", flush=True) #O flush=True serve para fazer a função sleeep funcionar dentro da função desligando o buffer de telça que fazia esperar o tempo e mostrar tudo de uma vez
        sleep(.5)
    print('')


contagem(1,10,1)

contagem(10,0,-2)


x= int(input('Início?'))
y= int(input('Fim?'))
z= int(input('Passo?'))

contagem(x,y,z)
