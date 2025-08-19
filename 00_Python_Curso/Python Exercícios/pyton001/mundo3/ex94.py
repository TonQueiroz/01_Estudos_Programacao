# Nome sexo e idade de várias pessoas
#Quantas pessoas cadastradas?
#Média de idade do grupo?
#Lista só com mulheres
#lista com todas pessoas com idade acima da média    

cadastro= []
pessoa = {}
mulheres = []
acimaidade = []

totp = idadetot = c = 0

while True:

    #LEITUDA DE DADOS
    pessoa['nome']  = str(input('Nome?'))
    
    while True:
        pessoa['sexo'] = str(input("Sexo?[M]/[F]")).upper()
        if pessoa['sexo'] in "MF":
             break
        print('ERRO! FAVOR DIGITAR M OU F.') #ESSE PRINT NÃO ENTRA SE O BREAK DO IF ENTRAR PQ TA DENTEO DO WHILE MAS DEPOIS DO BREAK QUE PARA O WHILE
        
    pessoa['idade'] = int(input('Idade?'))

    #COLOCANDO DADOS NA LISTA
    cadastro.append(pessoa.copy())
    pessoa.clear()
    totp +=1  # Total de pessoas cadastrradas ELE TROCOU O CONTADOR POR LEN(DICIONÁRIO) NÃO PRECISOU USAR ESPAÇO NA MEMÓRIA

    #Condição de saída
    saida = " "
    while saida not in "SN":
        saida = str(input('Quer continuar? [S] / [N]')) .upper().strip()[0]
    
    if saida == 'N':
        break

print(cadastro)

for i in cadastro:
    c += 1
    idadetot += i['idade'] # sOMA DE idade total do Grupo

    if c == len(cadastro):

        medid = idadetot/totp

    if i['sexo'] =='F':
        mulheres.append(i['nome'])

for i in cadastro:

    if i['idade'] > medid:
                
                acimaidade.append(i['nome'])

                acimaidade.append(i['idade'])

print(f' Foram cadastradas um total de {totp} pessoas')
    print(f' A media de idade das pessoas é {medid:5.2f}') #5 quantidade de caracteres .2 Quantidade de casas Decimais f formatação
print(f' as mulhees cadastradas são {mulheres}')
print(f' As pessoas com idade acima da mésia são {acimaidade}')


   
    
