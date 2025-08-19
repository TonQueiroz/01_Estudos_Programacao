#Ler varios numeros e colocar numa lista 
#Quantos foram digitados
#lista de valores decrescente
# se io valor 5 foi segitado e esta ou não na lista

lista = []
c= c5 =0

while True:
        n = int(input('Digite um valor'))
        lista.append(n)

        while True:
                saida= " "
                saida = str(input('Quer continuar? [S] / [N}')).upper().strip()[0]

                if saida in 'SN' :
                        break
                else:
                        print('Inválida')
                        
        if saida == "N" :
                break


for item in lista:
        if item ==5:
                c5 +=1


print(lista)
print('A quantidade de itens na lista foi ', len(lista))
print('A quantidade de 5 na lista foi ',c5)

#lista.sort(reverse=True)  #Jeito de ordenar a lista com Sort(METODO) e coloca ao contrario com rever=True, esse metodo altera a variavel lista para o resto do prgrama

print (f' a lista Em ordem decrescente ficou\n {sorted(lista)[::-1]}')#Jeito de ordenar a lista com Sorted (FUNÇÂO) e coloca ao contrario com fatiamento [::-1], altera a lista só para uso local e ela continua sendo a mesma no resto do programa
print(lista)
                        
                
                        
                



                
                
                          
                

 

        


        


                       
        


