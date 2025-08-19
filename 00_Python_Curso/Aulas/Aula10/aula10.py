'''nome = input('Qual o seu nome?')

if nome =='Ton':
    print('9Beutifull name! \n Bom Dia!')
else:
    print(f'Bom dia {nome} Feio!!')'''

n1 = float(input('Primeira nota?'))
n2 = float(input('segunda nota?'))

m = (n1+n2)/2

if m >= 7:
    print('Parabéns Você Passou!')

else:
    print('Se Fudeu!')

print(f'Sua média é {m:.1f}')