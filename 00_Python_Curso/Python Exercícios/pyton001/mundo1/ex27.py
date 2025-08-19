nome =  input('Qual seu nome?').strip()

listanome = nome.split()

pn = listanome[0]
un = listanome[len(listanome)-1]

print (f'Seu primeiro nome é {pn} e seu ultimo nome é {un}')
