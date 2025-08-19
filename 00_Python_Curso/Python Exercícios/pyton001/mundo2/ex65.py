'Crie um programa que leia varioos numeros inteiros até o usuários dizer que não quer mais continuar' 
'no final vai mostrar a média dos números qual o maior e o menos valor lido'

N =0
c=0
soma=0
mai=0
men=0

cond = 'S'

while cond == 'S':
        
        N = int(input('Digite um Número Inteiro'))
        # Média
        soma = N + soma
        c=c+1

        media = soma/c

        #Maior Número
         
        if mai < N:
                mai = N
        
        if men > N or  men ==0:
                men = N

        cond = input('Quer Continuar? [S] / [N]').upper()

print (f'''A soma de todos os números foi {soma}!
       A média de todos os Numeros foi {media}!
       O maior número foi {mai}!
       O menos npumero foi {men}!''')

