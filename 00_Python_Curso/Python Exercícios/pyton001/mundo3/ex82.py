#Ler varios numeros e colocar numa lista 
#2 listas extreas com valores pares e impares
#mostre as 3 listas geradas


lista = [ ]

listap = [ ]

listai = [ ]
while True:
        n= int(input('Digite um valor'))

        lista.append(n)

        while True:
                saida = input("quer continuar?[S] / [N]").upper().strip()[0]
                if saida not in 'SN':
                        print('valor invalido')
                else:
                        break
        if saida == "N":
                break

for item in lista:
        
        if item%2==0:
                listap.append(item)

        else:
                listai.append(item)

print(f'=-'*30)

print(f'{'LISTA PRINCIPAL'}\n {lista}')

print(f'=-'*30)
print(F'{'LISTA PAR'}\n {listap}')

print(f'=-'*30)
print(F'{'LISTA IMPAR'} \n {listai}')

print(f'=-'*30)