'''for c in range(6,1, -1): # O -1 FAZ ELE CONTAR SUBTRAINDO AO INVEZ DE ADICIONAR SE COLOCAR -2 ELE VAI DE 2 EM 2 
    print(c)
print('FIM')


for c in range(1,67, 6): # O -1 FAZ ELE CONTAR SUBTRAINDO AO INVEZ DE ADICIONAR SE COLOCAR -2 ELE VAI DE 2 EM 2 
    print(c)
print('FIM')

N = int(input('DIGITE UM NUMERO:'))

for c in range(0,N+1):
    print(c)
print('FIM')'''
#-------------------------------------------------------------
'''inicio = int(input('inicio:'))
fim = int(input('fim:'))
passo = int(input('passo:'))

for c in range(inicio, fim+1, passo):
    print(c)
print('FIM')'''

#-------------------------------------------------------------

n = int(input('Quantos numeros quer somar?'))
soma = 0

for c in range(0, n):
    ns = int(input('qual número vai ser somado?'))   
    soma+=ns # posso usar tbm --> soma+=ns ou soma = ns + soma
print(soma)  
print('FIM')