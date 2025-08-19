#TUPLAS

# ( ) TUPLAS com ou sem parenteses cria-se uma tupla
# [ ] LISTAS
# { } DICIONÁRIOS

lanche = ('Hamburguer',  'SUCO', 'PIZZA', 'PUDIM')


print (lanche[:2])

for c in lanche: #se não precisar mostrar a posição
    print ('eu vbou comer', c)


for pos, comida in enumerate(lanche): #pos e enumerate para mostrar a posição
   
    print(comida, ' na posição', pos)

    

for comida in range(0, len(lanche)): #conseguee mostrar posição tbm
    print(comida)
    print(lanche[comida])

print(sorted(lanche)) #organiza exibição em ordem alfabética numa lista mas não muda a tupla original ela continua existindo se jogar em uma variavel você cria uma nova lista


