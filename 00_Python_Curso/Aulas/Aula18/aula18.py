#Aula 18 Listas Compostas (listas dentro de listas

test=[]

test.append('gustavo')#aqui estou adicionando a uma lista
test.append(40)#aqui estou adicionando a uma lista

galera =[ ]

galera.append(test[:])#aqui estou adicionando uma lista a uma lista vazia 

test[0] = 'maria'
test[1] = 20

galera.append(test[:])#aqui estou adicionando mais uma lista que jpá tem uma lista 

print(galera)

 
galera2 = [['joão', 25],['maria', 20, ], ['pedro', 32]]#aqui estou Dclarando uma lista com outras listas 

print(galera2)

print(galera2[0]) #vai printar João 25

print (galera2[1][1]) #vai printar 20


for p in galera2:
    print ('-=-=-=\n',p[0])


###########################
# Adicionando listas nas listas com umm for

galera3 =[]
dado= [ ] #Vai servir poara receber temporariamente a lista que vai ser adicionada.
menoridade = maioridade=0
for c in range(0,3):
    dado.append(str(input('Nome?')))
    dado.append(int(input('Idade?')))
    galera3.append(dado[:]) #Não esquece do [:]
    dado.clear() #Limpa Lista

print(galera3)

for idd in galera3 :
    if idd[1] > 18:
        print(f'{idd[0]} é de maior')
        maioridade += 1
    else:
        print(f'{idd[0]} é menor de idade')
        menoridade += 1

print (f'Temos {maioridade} maiores de idade e {menoridade} menores de idade!')




