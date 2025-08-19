#desafio Ler 5 numeros
# inserir em uma lista  nas posições já ordenadas.

lista = []

for c in range (0,5):
        
                n = int(input(f'Digite o {c+1}º : ')) 
                
                
                if len(lista)==0 or n>lista[-1]: #len(lista) 0 significa que n tem nenhum item na lista  O, len vai de 1 a 5 não de 0 a 4 -- [-1] pega o ultimo item da lista
                        lista.append(n) #Adicionado ao final da lista

                else:
                        for pos in range(0,len(lista)):
                                if n < lista[pos]:
                                        lista.insert(pos, n) #Adicionado na posição específica
                                        break #break tbm funciona pra for


print ('Lista Ordenada \n',lista)


                

        


        


                       
        


