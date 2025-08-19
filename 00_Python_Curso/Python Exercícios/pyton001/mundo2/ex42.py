''' EXERCÍCIO 42 --- COMPLEMENTAR O 35

SE ELE PUDER FORMAR UM TRIANGULO, ACRESCENTANDO O RECURSO DE MOSTREAR QUE TIPO DE TRIALGULO SERÁ FORMADO

EQUILATERO : TODOS LADOS IGUAIS

ISÓCELES: DOIS LADOS IGUAIS

ESCALENO :  TODOS OS LADOS DIFERENTES'''

r1 = int(input('Qual o tamanho da primeira reta? /n'))

r2= int(input('Qual o tamanho da seguunda Reta? /n'))

r3= int(input('Qual o tamanho da terceiraa Reta? /n'))

if ((r1+r2) > r3) and  ((r1+r3)>r2) and ((r2+r3>r1)):
    cond = 1
    print(f'Você pode formar um triangulo!')
    print (f'e esse triagulo é!')

    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISÓCELES')
    elif r1 != r2   and r1 != r3   and r3 != r2:
        print('ESCALENO!')
        
else:
  
    print(f'Você nao pode formar um triangulo!')

