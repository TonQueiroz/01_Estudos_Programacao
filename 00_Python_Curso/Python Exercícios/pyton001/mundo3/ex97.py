# Função chamada escreva que receba um texto e mostre uma mensagem com um comando adaptavel

def titulo(tt):
    
    print('~'*(len(texto)+4))
    print(f'  {tt:^}  ')
    print('~'*(len(texto)+4))


texto = str(input('Digite um título'))

titulo(texto)

