#Ler quantos números o usuário quiser até ele pedir pra parar
# Se o número já existir ele não deixa adicionar
# no vfinal exiba os valores em ordem crescente.

lista = []


while True:
        while True:
                n = int(input('Digite um Número para acrescentar lista!'))
                
                if n in lista:
                        print ('Esse número ja existe na lista! Tente outro número')
                        
                else:
                        lista.append(n)
                        print('Adicionado com Sucesso!')
                        break
                        
        saida =" "
        while saida not in "SN":
                saida = input('Quer continuar?[s]/[n] ' ).upper().strip()[0]      
                if saida not in 'SN':  
                        print ('Digite um valor válido')

        if saida == "N":
                break

print(lista)

print(f'Lista ordenada!')

lista.sort() # ou {sorted(lista)}

print(lista)



