# Programa com Função chamda notas() Que pode receber várias notas de alunos e Retorna um dicionário com
#Quantidade de notas
#maior nota
# Menor nota
#Média da turma
#Situação
#Adicionar docstrings

def notas(*nt, situação = False):
    '''
    notas(*nt, situação = false)
        --> Função para analizar notas de alunos
        
        :para nt:  recebe nota ou Notas dos alunos
        :para situação: Recebe true para retornar a situação da turma ou false para não retornar
        
        :reutn: Retorna um dicionário com várias informações sobre as notas
    '''
    dic = {}
    dic['Total']= len(nt)
    dic['Maior Nota'] = max(nt)
    dic['Menor Nota'] = min(nt)
    dic['Média'] = sum(nt)/len(nt)

    if situação == True:
        if dic['Média']<5: 
            dic['Situação'] = 'péssimna'
        elif dic['Média']>=5 and dic['Média']<7: 
            dic['Situação'] = 'Boa'
        elif dic['Média'] >=7 and dic['Média']<=9:
            dic['Situação'] = 'Excelente'
        elif dic['Média']==10:
            dic['Situação'] = 'Extraordinária'

    return dic

dicionariodenotas = notas(4,8,10,10,5,7,8,10,1, situação=True)

print(dicionariodenotas)

