# Crie tupla com contagem de 0 a 20
# Ler um numero entre 0 e 20 e mostralo por extenso
# tratamento de exceções se ele não estiver entre 0 e 20

contagem = ("Zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    while True:
        n =  int(input('Qual número gostaria de ver?'))
        if n >= 0 and n<= 20:
            break
        else:
            print('Número Inválido Digite novamente')

    print("você digitou o número: \n", contagem[n].upper())

    while   True:  
        saida = input('Você gostaria de continuar? [S] / [N]').upper().strip()
        if saida in 'SN':
            break
        elif saida not in 'SN':
            print('Entrada Inválida Digite novamente')

    if saida == "N":
        break

print(' Obrigado! até mais! ')
        



