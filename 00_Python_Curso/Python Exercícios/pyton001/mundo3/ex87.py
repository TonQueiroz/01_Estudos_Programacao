#Crie uma matriz 3x3 e preencha os números com valores lidos, no final mostre a matriz na tela com a formatação correta EX 85
#Agora mostre a soma dos valores pares
#a soma dos valores da 3ª Coluna
#O maior valor da segunda linha

Matriz = []
soma= somacol3 = maxv =0

linha = []
for l in range (0,3): #Adicionando os números na pocição correta
        for n in range(0,3):
                n = int(input(f'Digito número da posição [{l},{n}] '))
                linha.append(n)
        Matriz.append(linha[:])
        linha.clear()

print('=-'*30)
                                        
for p  in range(0,len(Matriz)):        # Mostrando os Números na posição correta  #Colocando len(matriz) eu ajusto independente do tamanho da matriz por prga o a quantidade de itens dela
        for q in range(0,len(Matriz[p])):  #Colocando len(matriz)[p] eu ajusto independente do tamanho da lista dentro da matriz matriz por pga o tamanho  da lista dela
                print(f'[{Matriz[p][q]:^5}]', end=" ")

                if q == 2:
                        somacol3 += Matriz[p][q]
                        #p e q  nos for acima  são as posições nas listas p linhas e q colunas


        for r in Matriz[p]: # r aqui são os valores 
                if r%2==0:
                        soma+=r
                
                if p == 1:
                        if r > maxv:
                                maxv = r


                
                                
        print('')

print (f' A Soma dos valores pares é = {soma}')
print(f' A Soma dos valores pares da 3ª colunba é = {somacol3}')
print(f' O maior valor da segunda linha é = {maxv}')









    















