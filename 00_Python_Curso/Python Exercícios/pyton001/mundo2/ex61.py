'Refaça o desafio de progressão aritimética (51) faça utilizando o wile!'



pt = int(input('Digite o Primeiro Termo!'))
rz = int(input('Digite a Razão da progressão!'))

tm= int(input('Quantos termos da progressão gostaria de ver ?'))

pa = pt

c = 0

while c < tm:
    print (pa, end ="-")
    pa = pa + rz
    
    c = c+1
    