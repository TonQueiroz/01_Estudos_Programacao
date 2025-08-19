#Cadastro de pessoas

#Menu

c=( "\033[0m",  #SEMCOR = 0
    "\033[31m", #VERMELHO = 1
    "\033[32m", #VERDE = 2
   "\033[33m",  # AMARELO = 3
   "\033[34m"   #AZUL = 4
   ""    
    )

def linhal(x=40):
    print('-'*x)

def título (txt='título genérico', larg =40):

    linhal(larg)
    print (f'{txt:^40}'.upper())
    linhal(larg)



def menu(opções):
    '''Passe como parametro uma lista com opçoes nos itens 
    OBS: IMPORTANTE - Deixe por ultimo a saída do sistema '''
    while True:
        menud = dict()

        
        for c in range(1,len(opções)+1):
            menud[c]= opções[c-1]
                
        for k, v in menud.items():
            print(f'\033[33m{k} \033[34m{v:>35} \033[0m')

        
    
        
        escolha = (input('Escolha sua opção'))

        
        try:
            escolha = int(escolha)

        except:
            print ('\033[31mescolha invalida, tente uma opção numérica no menu.\033[0m')
            linhal(40)
            continue
        
        else:
            if escolha == max(menud.keys()):
                título('OBRIGADO POR USAR NOSSOS SERVIÇOS')
                return escolha
                

            elif escolha in range (1,len(menud)) :     
                linhal(40)
                título(menud[escolha])
                return escolha              
                
            else:
                print('sheet')
                título('Escolha invalida, tente uma opção numérica no menu.')                
                
      