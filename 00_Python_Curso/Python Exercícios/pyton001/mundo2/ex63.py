'Programa que leia um npumero inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia fibonacci ex = 0 - 1 - 1 -2-3-5-8'

N = 0

NA = N-1

elem = int(input('Quantos elementos da sequencia fibonacci deseja ver?'))

c=0

while  c < elem:
    print (N, end="-" )

    NF = NA + N

    NA = N

    N = NF

    c = c+1






