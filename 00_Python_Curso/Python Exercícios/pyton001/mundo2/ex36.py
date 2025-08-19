''' FINANCIAMENTO DE UMA cASA
SE QUALTO É A PARCELA? 
SE O VALOR DA PARCELA FOR >30% DO SALÁRIO , FINANCIAMENTO REPROVADO.'''


casa = float(input('Qual o valor da casa?'))
parc = float(input('em qualtas vezes gostaria de pagar?'))
sal = float(input('Qual o seu salário?'))

prest = casa/parc

salp = sal*0.3

print (f'A prestação ficaria{prest:.2f}.')

if prest <= salp:
    print('Parabéns o seu financiamento foi aprovado!')
else:
    print('Sinto muito, não podemos aprevar o seu financiamento para esse valor!')
