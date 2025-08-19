# Função chamda fatorial 
# recebe 2 parametros o número do fatorial e  show booleano(lógico) indicando se será mostrado ou nçao na tela o processo de calculo


def fatorial (num=1, show=False):
    '''
    --> Calcula o fatorial de um número
    :para n: O número a ser cauculado
    :para show: mostra ou não o cálculo do fatorial  

    :print: imprime o fatorial e o número caso o show for true
     
    :returne: não retorna nada '''
    f=1
    for c in range (num,0,-1):
        f*=c
        if show==True:
            print (c,end=' ')
            if c > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')

    return f

    

n = int(input('Qual número gostaria de ver o fatorial?'))
cond = int(input("gostaria de ver com detalhes? [1] SIM / [0] NÃO \n"))

if cond == 0 :
    cond = False
else:
    cond = True

print(fatorial(n,cond))
            
#help(fatorial)

    


    
    



