'''LEIA NOME IDADE E SEXO DE 4 PESSOAS E MOSTRE A MÉDIA DE IDADE QUAL O NOME DO HOMEM MAIS VELHO E QUANTAS MULHERES TEM MENOS DE 20 ANOS'''

totaldid =0
idmulheres = 0
idhomem = 0

for c in range (1,4+1):
    nome = input(f'qual o nome da {c}ª pessoa?')
    idade = int(input(f'qual a idade da {c}ª pessoa?'))
    sexo = int(input(f'qual o sexo da {c}ª pessoa?[1] Homem [2] Mulher'))

    
    #Média de Idade
    totaldid += idade
    medid = totaldid/4
   
    #Homem Mais velho
    if sexo == 1 and idhomem < idade:
        idhomem = idade
        nomehomemv = nome
    
    #mulheres com menos de 20 anos
    if sexo == 2 and idade <20:
        idmulheres += 1 

print( f'A média da idade das pessoas é {medid}')
print(f'A idade do homem mais vélho é {idhomem} e ele chama {nomehomemv}')
print(f'A quantidade de mulheres com menos de 20 anos é {idmulheres}')


