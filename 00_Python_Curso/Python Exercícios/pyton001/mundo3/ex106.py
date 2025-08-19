# Mini sistema que utilize o interactiv hgelp do Python. O usuário vai digitar o comanoe o manual vai aparecer
#Quantidade de notas
#Quando o usuário digitar fim o cprograma se encerrará
#Obs Use cores

def título(txt):
    print('~'*len(txt))
    print(txt)
    print('~'*len(txt), end=" ")



def ajuda():
    '''
    --> ajuda()

    Descrição
    Ajuda é uma função para utilizar o help do python sobre qualquer função, comando atributo, classe e muito mais.

    

    '''
    while True:
        print("\033[37;45m")
        título (F'{'  SISTEMA DE AJUDA PYHELP  '}') 
        print("\033[0m")  

        função = input('Sobre qual função da biblioteca precisa de ajuda? > ').lower().strip()
        print("\33[37;44m")
        título (f'  Acessando o manual do comando {função}.  ')
        print('\33[0m')
        
        print('\33[30;47m')
        help(função)
        print('\33[0m')

        saida = " "
        while saida not in "SN":
            saida = input('Gostaria de cotinuar?[S] / [N]').upper() .strip()[0]
            
        if saida in 'N':
            break
   

ajuda()
print("\033[37;41m")
título('  OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS. ATÉ LOGO.  ')
print("\033[0m")


    

