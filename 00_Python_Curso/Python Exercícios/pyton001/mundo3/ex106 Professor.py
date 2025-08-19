# Mini sistema que utilize o interactiv hgelp do Python. O usuário vai digitar o comanoe o manual vai aparecer
#Quantidade de notas
#Quando o usuário digitar fim o cprograma se encerrará
#Obs Use cores

c = ('\033[m',      # a cor 0 é sem cores
       '\033[37;45m', # a cor 1 é fundo rosa letra branca
       "\33[37;44m",  # a cor 2 é fundo azul letra branca
       '\033[37;41m',  # a cor 3 e é fundo vermelho letra branca
       '\33[30;47m'  #  4 fundo branco
       )

def título(txt, cor = 0):

    print (c[cor])
    print('~'*len(txt))
    print(txt)
    print('~'*len(txt), end=" ")
    print (c[0])



def ajuda():
    '''
    --> ajuda()

    Descrição
    Ajuda é uma função para utilizar o help do python sobre qualquer função, comando atributo, classe e muito mais.


    '''
    while True:
        
        título ('  SISTEMA DE AJUDA PYHELP ', 1) 
          

        função = input('Sobre qual função da biblioteca precisa de ajuda? > ').lower().strip()
        
        título (f'  Acessando o manual do comando {função}.  ', 2)
        
        
        print(c[4])
        help(função)
        print(c[0])

        saida = " "
        while saida not in "SN":
            saida = input('Gostaria de cotinuar?[S] / [N]').upper() .strip()[0]
            
        if saida in 'N':
            break


   

ajuda()

título('  OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS. ATÉ LOGO.  ', 3)



    

