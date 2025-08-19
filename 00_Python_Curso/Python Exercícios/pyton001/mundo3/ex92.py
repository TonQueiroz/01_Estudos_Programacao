#Leia nome, Ano de nascimento e carteira de Trabalho
#Cadastre com idade em um dicionário
#se a carteira de trabalho foor diferente de ZERO
#o dicionário receberá também o ano de contratação e o salário da pessoa
#Calcule ae acrescente além da idade o ano que a pessoa vai se aposentar



from  datetime import datetime

dados = {}

dados['nome'] = str(input('Nome?'))
anonasc = int(input('Ano de Nascimento?'))
dados['idade'] = ((datetime.now().year)-(anonasc))
dados['carteira de trabalho'] = int(input('número da carteirra de trabalho "Se não tiver = [0]"?'))

if dados['carteira de trabalho'] != 0 :
    dados['ano contratação']= int(input('Em qual ano foi contratado?'))
    dados['salário'] = int(input('Quanto é os seu salário ?'))
    dados['aposentadoria'] = (dados['ano contratação']+35)-anonasc

for k,i in dados.items():
    print(f' -- O {k} tem o valor {i}')




