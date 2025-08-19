# Condições ANINHADAS

'''nome = str(input('Qual é seu nome?'))

if nome=='Ton':
    print (f'Que nome bonito {nome}')
elif nome == "pedro" or nome == "maria " or nome == "joão":
    print('que nome comum!')    
elif nome in 'Ana Claudia Jessica Juliana':
    print('que nome bomito feminino')
else:
    print('seu nome é normal')
print (f'Bom Dia, {nome}')'''

ValorCasa = float(input ('Qual o valor da casa?')) 

Entrada = float(input('qual o valor da entrada?'))

ValorFinanciamento = ValorCasa - Entrada

print ('Você vai financiar', ValorFinanciamento)

Sal = float(input("Qual o seu salário?")) 

TempoFinanciamento = float(input("Em quantos anos gostaria de pagar o financiamneto?"))

parcela = ValorFinanciamento / (TempoFinanciamento*12)

sal30 = (Sal*0.30)

if parcela < sal30:
    print(" Seu finianciamento foi aprovado! com parcelas de", parcela)
elif parcela == sal30:
    print('deu na medida ein cuzão!')
else:
    print("Seu financiamento não foi aprovado pelo valor da parcela ", parcela," Ser maior que ", sal30, "que é 30 porcento do seu salário.")