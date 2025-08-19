'''LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALINDRONO (FRASE QUE SE LE A MESMA COISA DE TRAS PRA FRENTE "APOS A SOPA") DESCONSIDERANDO OS ESPAÇOS'''
'''
lista= []
frase = input('Digite a frase \n')

frase1  = frase.split()

fj="".join(frase1)

'''
'''fi = ''.join(reversed(fj))
print (fi)

if fj == fi:
    print('A frase é uma palíndroma!')
else:
    print('A frase NÃO é uma palíndroma!')'''

'''for c in range (len(fj)-1,0-1, -1):
    lista.append(fj[c])

fi = ''.join(lista)
print (fi)

if fi == fj:
    print (f'A frase {frase} é um palindromo!')
else:
    print(f'A frase {frase} não é um palindromo!')'''
    

#EXERCÍCIO PROFESSOR

frasep = str(input('Digite a Ffrase pra saber se é um palindrono')).strip().upper()
 
palavras = frasep.split()

juntas = "".join(palavras)

invertida = ''

for letra in range (len(juntas)-1, -1, -1):
    invertida += juntas[letra]

print(juntas)

print(invertida)

if invertida==juntas:
    print(' a frase é um palindrono')
else:
    print(' a frase NÃO é um palindrono')