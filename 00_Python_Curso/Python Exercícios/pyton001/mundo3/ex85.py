#Ler 7 valores numéricos cadastre em uma unica lista que mantenha separado os valores pares e impares
# A ) no final mostre os valores em ordem crescente


lista = []

pares= []
impares=[]

for n in range(0,7):
        num = int(input('Número?'))
        lista.append(num)

print(lista)

for item in lista:

        if item%2==0:
                pares.append(item)

        else:
                impares.append(item)




print('lista par \n', sorted(pares))


print('lista impar \n', sorted(impares))










