def metade (prc):
    x = prc/2
    return x

def dobro(prc):
    x = prc*2
    return x

def aumento(prc):
    x = prc*1.1
    return x

def reducao(prc):
    x= prc*0.85
    return x

def moedaf(prc = 0 , moeda='R$'):
    return f'{moeda}{prc:>8.2f}'.replace('.',",")

