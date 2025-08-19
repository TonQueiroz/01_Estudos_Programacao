'''Diga se o Ano é bissexxto'''

'''
ano = int(input('Qual ano você gostaria de saber se é bissexto ?'))

anostr = str(ano)

if (ano%4) == 0 and anostr[len(anostr)-2:]!='00' :
    print(f' O Ano de {ano} é Bissexto')

elif anostr[len(anostr)-2:] =='00' and (ano%400)==0:
    print(f' O Ano de {ano} é Bissexto')

else:
    print(f' O ano de {ano} não é Bissexto!')
'''

    # Código Professor Simples

from datetime import date

anop = int(input('Qual Ano Quer Analisar? Digite 0 para analizar o ano atual'))

if anop == 0:
    anop = date.today().year

if anop %4 == 0 and  anop % 100 != 0 or anop % 400 == 0:
    print(f'O ano {anop} é Bissexto!')
else:
    print(f'O ano {anop} não é bissexto')

