

import moeda


p = int(input('digite o preço...'))
print(f'Metade de {moeda.moedaf(p)} = {(moeda.metade(p, True))}')
print(f'Dobro de {moeda.moedaf(p)} = {(moeda.dobro(p, True))}')
print(f'Aumento 10 % de {moeda.moedaf(p)} = {(moeda.aumento(p, 10, True))}')
print(f'Redução de 15% de {moeda.moedaf(p)} = {(moeda.reducao(p,20, True))}')