
from pacotes import dado as d, moeda as m

p = d.validadorisfloat()

print ('-'*30)
print (f'{'RESUMO DO VALOR':^30}')
print ('-'*30)


print(f'{'Preço analizado:':<20}{m.moedaf(p):>10}')
print(f'{'Metade do preço:':<20}{(m.metade(p, True)):^10}')
print(f'{'Dobro  do preço:':<20}{(m.dobro(p, True)):^10}')
print(f'{'Aumento de 10%:':<20}{(m.aumento(p, 10, True)):^10}')
print(f'{'Redução de 15%:':<20}{(m.reducao(p, 15, True)):^10}')

print ('-'*30)