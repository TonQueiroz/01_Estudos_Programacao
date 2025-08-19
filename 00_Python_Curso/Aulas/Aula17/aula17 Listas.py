#Aula 17 Listas
num = [2,5,9,1]

print(num)

num[2] = 3

print (num)

num.append(7)

print (num)

num.sort()
print (num)

num.sort(reverse=True)
print (num)

print(f'Essa lista tem {len(num)} elementos')'

num.insert(45, 4)
print (num)

num.pop(2)   #Vai remover na posição 2
print (num)

num.remove(2)  #vai remover o número 2 se ele estiver na lista
print (num)

valores= list()

valores.append('A')
valores.append("B")
valores.append("c")
valores.append("d")

print(valores)

for c , I in enumerate(valores): #Enumera a posição dos valores/itens da lista
    print(f' posição {c}  Item {I}')  


for c in range(0,5):
    valores.append(int(input('Adicione um valor a lista Valores'))) #adiciona 5 valores a lista'''

print(valores)

listaa =[1,2,3,4] 
listab = listaa #Se você ffizer assim, quando nmmudar um item da lista b muda um da lista A pois elas ficam interligadas como uma
listac = listaa[:] #assim, é como se você tivesse criando uma lista nova com os itens da lista A e quando nmmudar um item da lista c NÂO muda um da lista A.

listac.append('A')

print(f'lista a {listaa}')
print(f'lista b {listab}')
print(f'lista c {listac}')