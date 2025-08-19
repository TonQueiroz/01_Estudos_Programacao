'Programa que leia varios numerros inteiros e só para quando digitar 999! no final mostre quantos numeros foram digitados e soma entre eles descontando a flag 999' 

SN = c=0

N = int(input('Diga um número inteiro'))
while N != 999:
                
        #SOMA DE N'S
        SN = SN +N

        c = c+1

        N = int(input('Diga um número inteiro ou 999 para parar'))

print('''Você digitou {} Números 
    A Soma dos números digitados é{}'''.format(c, SN))