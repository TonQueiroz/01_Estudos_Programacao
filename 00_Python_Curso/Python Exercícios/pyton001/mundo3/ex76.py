#TUPLA COM NOMES DE PRODUTOS E PREÇOS SEGUIDOS
#MOSTRE UMA LISTAGEM COM OS PREÇOS ORGANIZADOS DE FORMA TABULAR


tupla=  ('PÃO', 1.50 , "LEITE", 4.00 , 'BOLACHA', 2.50,'bolo', 35.00,  )

print ('-=' *30)
print('LISTAGEM DE PREÇO')
print ('-=' *30)

'''print( f'{tupla[0]}.................R${tupla[1]}')
print( f'{tupla[2]}.................R${tupla[3]}')
print( f'{tupla[4]}.................R${tupla[5]}')
    '''


'''for c in range(0,len(tupla),2):
    print(f'{tupla[c]}.................R${tupla[c+1]:.2f}')'''

print ('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}') #^ cENTRALIZADO  - 40 EM POSIÇÕES/CARACTERES ESSAS FORMATAÇÕESN TEM QUE ESTAR DENTRO DE UMA F' COM UM {}
print ('-'*40)
for pos in range(0,len(tupla)):
    if pos %2 == 0 :
        print(f'{tupla[pos]:.<30}R$',end=" ")  #< ALINHADO A ESQUERDA - 30 POSIÇÕES/CARACTERES
    if pos%2 == 1:
        print (f'{tupla[pos]:>7.2f}') #> ALINHADO A DIREITA - 7 POSIÇÕES/CARACTERES

print ('-'*40)
    



    
