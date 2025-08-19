#Qualtos valores foram digitados e a soma entre eles até digitar 999!

Soma = c = 0

while True:

    n =  int(input('Digite um valor'))

    if n == 999: #Condição de parada
        break

    Soma += n
    c +=   1

print (Soma,'Aquantidade de números digitados foram ', c )