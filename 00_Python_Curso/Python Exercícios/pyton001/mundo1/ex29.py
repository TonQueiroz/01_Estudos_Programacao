'''Escreva um programna que leia a velocidade do carro e se ele 
estiver acima de 80 km/h, diga que ele recebeu 7 reais de multa por cada km a mais!'''


vel = int(input('Qual sua velocidade?'))



if vel > 80 :
    mul = (vel-80)*7
    print(f'Você está acima da velocidade e recebeu uma multa de R${mul:.2f}')
else:
    print (' ótimo, continue sua viagem com segurança dentr dos 80km/h')

print('--Fim--')