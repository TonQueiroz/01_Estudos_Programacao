'''Essas 3 retas foremam um triangulo ?'''

r1 = int(input('Qual o tamanho da primeira reta?'))

r2 = int(input('Qual o tamanho da segunda reta?'))

r3 = int(input('Qual o tamanho da segunda reta?'))


if (r1 + r2) > r3 and (r2+r3) > r1 and (r1 +r3)> r2:

    print(f' podemos fazer um triangulo com essas 3 retas!')
else:
    print(f' não podemos fazer um triangulo com essas 3 retas')
