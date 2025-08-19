''' FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENRO DE UM JOVEM E INFORME DE ACORDO COM SUA IDADE

SE ELE AINDA VAI SE ALISTAR
SE É A HORA DE LE SE ALISTAR
SE JÁ PASSOU DA HORA DE ELE SE ALISTAR

E QUANTO TEMFO FALTA OU PASSOU DO PRAZO'''

from datetime import date

cond = int(input( 'Você já se alistou para o exercito? [1] Sim [2] Não'))

if cond == 2 :

    datahoje = date.today()

    anonascimento = int(input('Em que ano você nesceu?'))

    idade = datahoje.year - anonascimento

    if idade < 18 :
        print ('Falta {} anos para você se alistar e servir seu país nas forças militares'.format( 18 - idade))

    elif idade == 18 :
        print ('É hora de você se alistar e servir seu país nas forças militares')
        
    else :
        print ('já passou {} anos para você se alistar e servir seu país nas forças militares '.format(idade - 18))

elif cond == 1: 

    print ('PARABEN! Você está em dia com o serviço militar do seu país')