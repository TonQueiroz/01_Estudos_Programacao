#Aula 21 Funções 2 

#INTERACTIVE HELP

#help() Função para chamar

#help()


def contador(i, f , p=1):  # PARAMETROS OPCIONAIS p =1  se você não declarar a variavel p nba chamada da função ela vai entrar no programa como 1
    """ #DOC STRING - Documentação que vai entrar no comando help() ou no atributo .__doc__ se um deles  for chamado sobre contador.
    Contador com escolha de passo: 
    :i =  início
    :f = Fim
    :p = Passo    
    Não retorna nenhum valor
    """
    
    for c in range(i,f,p):
        print(c)

help(contador)

#Escopo de variaveis

def contador(i, f , p=1):  # Escopo de variaveis
  
    
    for c in range(i,f,p): #Variaveis locais declaradas dentro de funções só funcionam alí mesmo, fora não funcionam i, f, p
        print(c)

a = 5
b = 10
c =2
#VARIAVEIS GLOBAIS 5 10 e 2 Declaradas no escopo global e servem no programa todo

contador(a,b,c)
#Se eu mudar o valor de uma variavel global num escopo local ela muda apenas no escipo local 
#quando voltar ao programa principal ela volta ao valor local


def contador(i, f , p=1):  
    global a #Assim você posde alterar a variavel Global  a de dentro da função!
  
    
    for c in range(i,f,p): 
        print(c)

a = 5
b = 10
c =2


#RETORNO DE VALORES

def somar (a,b):
    s=a+b
    return s # assim retorna o resultado para a variavel referenciada definida quando chamou a funçãio(#1) ou para um print(#2)

 #variavel referenciada definida quando chamou a funçãio(#1)
r1 = somar(2,5)  # Assim retorno o valor das funções para variaveis diferentes
r2 = somar(12,33)
r3 = somar(2123123,4322)

print(somar(1,10))# print(#2) definida quando chamou a funçãio

print(f'O retorno das funçoes em variaveis diferentes foram -- > {r1} {r2} {r3}')


