def metade (prc , formato = False):
    x = prc/2

    if formato == False: #SE FORMATO = TRUE  CHAMA A FUNÇÃO MOEDA F LÁ EMBAIXO
        return x  
    else: 
        return moedaf(x) 

def dobro(prc, formato = False):
    x = prc*2

    if formato == False:
        return x  
    else: 
        return moedaf(x)

def aumento(prc= 0 , taxa = 0, formato = False):
    x = prc + (prc*taxa/100)
    if formato == False:
        return x  
    else: 
        return moedaf(x)

def reducao(prc, taxa = 0, formato = False):
    x= prc - (prc*taxa/100)

    if formato == False:
        return x  
    else: 
        return moedaf(x)

def moedaf(prc = 0 , moeda='R$'):
    return f'{moeda}{prc:>8.2f}'.replace('.',",")
