

import moeda


p = int(input('digite o preço...'))
print(f'Metade de {moeda.moedaf(p)} = {moeda.moedaf(moeda.metade(p))}')
print(f'Dobro de {moeda.moedaf(p)} = {moeda.moedaf(moeda.dobro(p))}')
print(f'Aumento 10 % de {moeda.moedaf(p)} = {moeda.moedaf(moeda.aumento(p))}')
print(f'Redução de 15% de {moeda.moedaf(p)} = {moeda.moedaf(moeda.reducao(p))}')