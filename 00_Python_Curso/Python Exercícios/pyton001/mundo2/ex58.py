'Melhore o jogo do ex 28 só que agr entre 0 e 10 que só para quando o computador adivinhar e mostra quantas tentativas você precisou para acertar!'


from random import randint

Lista = [1,2,3,4,5,6,7,8,9.10]

comp = randint(1,10)

Jogador = 0

acertou =  False

while not acertou :
        Jogador = int(input('Escolha um Número de um a dez!'))
        if Jogador <=10 and Jogador>=1:
            if Jogador != comp:            
                print ('ERROU! Tente outra vez!')
            else:
                print(f'Você Acertoooo! O número escolhido pelo computador foi {comp}')
                acertou = True
        else: 
             print('Entrada Inválida! Tente outro número que seja de um a dez')  


print ("Ótimo, até a proxima")