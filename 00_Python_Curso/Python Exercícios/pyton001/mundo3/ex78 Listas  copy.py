#Ler 5 numeros, colocar numa lista mosdtrare o maior o menor e suas posições.
lista = list()
for c in range (1,6):
        lista.append(int(input(f'Digite o {c}º número')))
   


print ('-='*20)
print (lista)

print ('-='*20)

print (f'Menor número {min(lista)}, posição, {lista.index(min(lista))}')

print ('-='*20)

print (f'Maior número {max(lista)}, posição {lista.index(max(lista))}')

print ('-='*20)
