'Leia um número qualquer e mostree seu fatorial Ex > 5! = 5x4x3x2x1 = 120'

v = int(input(' Quer saber o fatorial de Quel número ?'))

n = v

fat = n

while n > 0:
    print (n,  end = " ")
    print('x' if n > 1 else'=', end=' ')
    
    fat = fat * (n)
    
    n=n-1
    

print(f'\n O Fatorial de {v} é {fat}')
    
