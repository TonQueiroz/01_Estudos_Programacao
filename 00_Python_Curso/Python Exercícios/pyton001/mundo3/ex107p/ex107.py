import moeda


p = int(input('digite o preço...'))

print(f'Metade de {p} = {moeda.metade(p)}')
print(f'Dobro de {p} = {moeda.dobro(p)}')
print(f'Aumento 10 % de {p} = {moeda.aumento(p)}')
print(f'Redução de 15% de {p} = {moeda.reducao(p)}')
