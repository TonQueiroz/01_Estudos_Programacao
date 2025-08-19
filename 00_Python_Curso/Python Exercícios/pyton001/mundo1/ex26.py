nome = input('Escreva seu nome?').strip().lower()

qa = nome.count('o')

ppn = nome.find('o')

upn = nome.rfind('o')

print ('A quantidade de letras o é ', qa, '\n Primeira Posição da letra o', ppn+1,  '\n Ultima Posição da letra o', upn+1)