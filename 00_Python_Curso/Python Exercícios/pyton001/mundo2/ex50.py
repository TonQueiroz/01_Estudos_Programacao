'''LER SEIS NÚMEROS INTEIROS E MOSTRE A DOMA DOS VALORES APENAS DOS NUMEROS PARES'''

soma = 0

for c in range (1,6+1):
    N = int( input(f'Digite o {c}º de 6 números para saber a soma dos número pares'))
    if N%2 == 0 :
        soma += N
  
print(soma)