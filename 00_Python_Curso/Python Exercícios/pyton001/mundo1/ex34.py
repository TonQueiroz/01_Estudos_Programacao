'''Salário e Aumento se vc ganha mais de 1250 reais +10% se você ganha menos +15%'''

salant = float(input('Qual é seu salário?'))

sal = salant

if sal >= 1250 :
    sal = sal * 1.1

else:
    sal = sal * 1.15

print (f'Você recebeu um aumentol, seu antigo salário éra R${salant:.2f} agora seu novo salário é de R${sal:.2f}')
