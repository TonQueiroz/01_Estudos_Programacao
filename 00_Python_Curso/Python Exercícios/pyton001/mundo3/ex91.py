#4 jogadores jogam um dado e tem resultados aleatórios
#Grardi os resultados em um dicionário
#No final coloque esse dicionário em ordem.
#O vencedor tirou o maior número do dado



from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
resultados = []
ranking = {}

for c in range (1,5):
    jogadores[f'Jogador{c}'] = randint(1,6)
    
resultados.append(jogadores.copy())

for  i in resultados:        
        
        for k, v in i.items():
                sleep(.5)
                print(f'o {k} tirou {v}' )

        print('---RANKING DOS JOGADORES---')
ranking = sorted(jogadores.items(), key=itemgetter(1))#itemgetter é importado da biblioteca operator serve para ordenar aliata atraves do item escolhido no caso o (1) a pontuação dos jogadores


ranking.reverse()
for p,i in enumerate(ranking):

       print (f'Na posição {p+1} ficou o jogador{i[0]} com  {i[1]} pontos!')




        