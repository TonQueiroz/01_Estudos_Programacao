#PROGRAMA DE CADASTROS
from modulos.menu import *    
from modulos.arquivo import *
from modulos.uteis import *

arq = 'cadastro.txt'

if not arquivoexiste(arq):# Essa função ta retornando True ou False Assim é como se #if aquivo existe == false # se não tivesse o not era #if arquivo existe ==True    
    criararquivo(arq)
else:
    print(' ')

listaopçõesmenu=['Ver pessoas cadastradas',
                 'Cadastrar nova pessoa',
                 'Sair']
while True :    
    resposta = menu(listaopçõesmenu[:])

    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        título('NOVO CADASTRO')
        nome = str(input('Nome do novo Cadastro?'))
        idade = leiaint(input('Idade do novo cadastro?'))
        
        
        cadastrar(arq, nome, idade)

    elif resposta ==3:
        break

    else:
        print('resposta Errada')
    
        
    










