#Ajude o jogador da mega a criar palpites
#pergunte quantos jogos serão gerados e sorteie nºs entre 1 e sessenta para eles
#cadastre os jogos em uma lista composta

from random import randint

listadejogos = []
listatemporaria = []

contadorrepetido = 0

jogos = int(input('Quantos jogos ?'))

for j in range(0,jogos):

                                               
        while len(listatemporaria) < 6 :
                n = randint(1,60)

                if  n not in listatemporaria :
                        listatemporaria.append(n)

                                
        listatemporaria.sort()                    
                
        
        listadejogos.append(listatemporaria[:])

        listatemporaria.clear()

for i, s in enumerate(listadejogos, start=1):
        print(f'O jogo {i} foi {s}')

          









    















