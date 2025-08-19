#Idade e sexo de varias pessoas! quantas pessoas +18, quantos homens e mulheres com menos de 20 anos!

cid = csx = cm20 = 0
while True:
    
    nome = str(input('Nome?'))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Sexo? [M]/[F]')).upper().strip()[0]
        
        
    idade = int(input('Idade:?'))

    #quantas pessoas +18
    if idade > 17:
        cid += 1
    
    #quantos homens
    if sexo == "M":
        csx += 1

    
    #mulheres com menos de 20 anos
    if sexo == "F" and idade < 20 :
        cm20 += 1

    #Condição de saída!
    while conti not in 'SN':
        conti = input('Quer continuar? [S] / [N]').upper().strip()[0]
        
    if conti == "N":
            break
print (f'Maiores de 18 anos = {cid}')

print (f'Quantidade de Homens = {csx}')

print (f'Mulheres de <20 anos = {cm20}')


