#leia Nome e Média de um aluno Se for maior que 7 guarde a situação aprovado
#no finalmostre o contreúdo na tela



Alunos = {} #ou dict()
          
Alunos['nome'] = str(input('Nome aluno'))
Alunos['média'] = float(input('Média'))

if Alunos['média'] >= 7 :
        Alunos['Situação'] = 'Aprovado'

else:
        Alunos['Situação'] = 'Reprovado'

print(Alunos)

print(f'O Aluno {Alunos['nome']} tirou a média {Alunos['média']} e foi {Alunos['Situação']}!')


    















    















