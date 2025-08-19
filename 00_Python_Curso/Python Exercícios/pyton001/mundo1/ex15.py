d=int(input('Quantos dias vc ficou com o carro alugado?'))
km=float(input('quantos km você rodou?'))

td = d*60
tkm = km*0.15

print('Ok, estou calculando...\n O valor pela diária do carro ficou R${:.2f} por {} dias \n O valor pela quantidade de KM ficou{:.2f} por {} Km\n O total da sua conta ficou R${:.2f}'.format(td, d, tkm, km, td+tkm))
