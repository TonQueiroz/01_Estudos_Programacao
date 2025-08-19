#Identificação da cidade Santo

cidade = input('Qual sua cidade?').strip()

print (cidade)

n1 = cidade.lower().split()

print('Voce mora em uma cidade que o nome começa com Santo?\n','santo' in n1[0])  

#Do professo


print ('Você mora em uma cidade que começa com santo?', (cidade[:5].lower() == 'santo'))
