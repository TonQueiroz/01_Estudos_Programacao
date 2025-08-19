'''Cobre a viagem de um Onibus por KM   até 200km é 50 centavos passou de 200km é 45 centavos por km'''


km = float(input('Quantos quilometros você vai viajar de ônibus?'))

if km <= 200:
    p = (km*50)/100
    print(f'Sua passagem custará \n R${p}.')
else:
    p = (km*45)/100
    print (f'Sua passagem custará \n R${p}')

print('--Fim do Orçamento 1')

# Código Simplificado

p = km * 0.50 if km<=200 else km * 0.45

print (f'Sua passagem custará \n R${p}')

print('--Fim do Orçamento 2')