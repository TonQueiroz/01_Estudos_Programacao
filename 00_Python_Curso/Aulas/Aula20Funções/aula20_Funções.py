#Aula 20 Funções
# Função
def soma(a, b):
    s = a + b
    print (s)


#Programa princpal

soma(4,5)

soma(5,10)

soma(45,1023)

#empacotamento quando vc n sabe a quantidade de parametros a passar

def empacotada(*num):
    print (num)

empacotada(1,3,4,43,35) #assim vc passa os número como uma tupla para a função e vc maneja ela como uma tupla comum

#Para passar LISTAS poe elas em uma variavel
listasaída = []
def dobralista(x):
    for c in lista:
        listasaída.append(c*2)

    print(listasaída)

lista= [32,33,45,22,176]

dobralista(lista)

print (lista)