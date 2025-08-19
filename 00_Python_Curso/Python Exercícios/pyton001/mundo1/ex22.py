nc = input('Qual seu nome completo ?')

print ('Nome em maiúscula = {}'.format(nc.upper()))

print ('Nome em minúsculas = {}'.format(nc.lower()))

print(nc)

nomeemlista = nc.split()

nomecompjunto = ''.join(nomeemlista)

print(len(nomecompjunto))


print('A quantidade de caracteres sem espaço é = {}'.format(len(nomecompjunto)))

print('O 1º nome tem a quantidade de letras de {}'.format(len(nomeemlista[0])))