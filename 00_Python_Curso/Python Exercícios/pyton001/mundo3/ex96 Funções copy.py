# Crie um programa que use funções para medira a área de um terreno

def area(a,b):
    print(f'{'Controle de Terrenos':^40}')
    print('-'*40)
    areaterreno = a*b
    print(f' A área do terreno com largura {a} e comprimento {b} é {areaterreno}m² ')


m1 = int(input('Qual o a dimenção da fachada? '))

m2 = int(input('Qual o a dimenção da profundidade? '))

area(m1 ,m2)

