'''contagem reguressiva de 10 a 1 para estouro de fogos de artifício! com espera de 1 segundo entre eles!'''

from time import sleep

start = int(input('''De quanto quer o Temporizador?'''))


for c in range (start , -1, -1):
    sleep (1)   
    print (c)