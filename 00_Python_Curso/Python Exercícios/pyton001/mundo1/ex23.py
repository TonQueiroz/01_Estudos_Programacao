#Destrinchando números

n = input('Escolha um numero de 0 a 9999: ')

print(f'Unidade: {n[3]} \nDezena: {n[2]} \nCentena: {n[1]} \nMilhar: {n[0]} ')

#Com Numeros inteiros


nn =int(n)

u = nn//1%10
d =nn//10%10
c = nn//100%10
m = nn//1000%10


print(f'Unidade: {u} \nDezena: {d} \nCentena: {c} \nMilhar: {m}')