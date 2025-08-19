from modulos.menu import *

def arquivoexiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close

    except FileNotFoundError:
        return  False

    else:
        return True
    
def criararquivo(arquivo):
    try:
        a= open(arquivo, 'wt+') #wt+ write = escreva t = arquivo de texto + = Se ]ao existir cria o arquivo
    except:
        print('OUVE UM ERRO NA CRIAÇÃO DO ARQUIVO')
    else:
       print('ARQUIVO CRIADO COM SUCESSO')

def lerarquivo(arquivo):
    try:
        a = open(arquivo,'rt')
    except:
        print("Não foi possivel ler o arquivo")
    else:
        título('PESSOAS CADASTRADAS')
        for l in a:
            dado = l.split(";") #splite separa as palavras onde ha ";" por que foram escritas assim no arquivo
            dado[1]=dado[1].replace('\n','')
            print (f'{dado[0]:<20}{dado[1]:>20}')
            
    finally:
        linhal()
        a.close

def cadastrar(arquivo, n , i):
    try:
        a= open(arquivo, 'at')
    except:
        print("Não foi possivel ler o arquivo")
    else:
        try:
            a.write(f'{n};{i}\n')
        except:
            print('OUVE UM ERRO NA CRIAÇÃO DO ARQUIVO')
        else:
            print(f'Nome e idade de {n} cadastrado com sucesso.')
    finally:
        a.close
        
