'''LEIA UM NÚMERO E DIGA SE ELE É PRIMO'''
#minha solução mais complicada
'''n = int(input('Qual número você quer Saber se é primo ?'))
nãoprimo = 0
''''''if n > 1 and n%2!=0  and n%3!=0 or n==2 or n==3 :
    print (f'O número {n} é primo!')
else:
    print (f'O número {n} é NÃO primo!')'''
'''
print ('-=-=-=-=-=-=-')

if n >= 1 and n!= 2 and n!=3 :
    if n==1:
        nãoprimo=1

    else:
        for c in range(2,n):         
            if n%c==0:
                nãoprimo=1   
        
if nãoprimo==1:
    print (f'O número {n} é NÃO primo!')
elif nãoprimo==0 or n!= 2 or n!=3:
    print (f'O número {n} é primo!')'''


print ('-=-=-=-=-=-=-')

# do professor muito mais rápído rs


n = int(input('Qual número quer saber se é primo ?'))
tot=0

for c in range (1,n+1):
    if n%c==0:
        tot+= 1
        print('\033[33m', end='')
    else:
        print ('\033[31m', end='')
    print(f'{c}', end='->')
if tot ==2 :
    print ('Esse número é primo')

else:
    print('Esse número não é primo!')

print('\033[00m')
