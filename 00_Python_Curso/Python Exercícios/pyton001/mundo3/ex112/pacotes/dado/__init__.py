def validadorisfloat():
    '''
    --> Usado para validar se o número é realmente um número
    : return: retorna o número se ele é realmente um número.
    '''
    while True:
        validador = False
        n = str(input('digite o preço...')).replace(',','.')

        try:
            float(n)
            n= float(n)
            validador = True

        except ValueError:
            print('não é um valor válido! digite um número')
        
        if validador == True:
            break

    return n