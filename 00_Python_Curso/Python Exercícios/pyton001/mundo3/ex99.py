# Função chamada MAIOR com varios parâmetros com valores inteiros INÍCIO, FIM E PASSO 
# Seu programa tem que análisar todos os valores e dizer qual o maior

from time import sleep

def maior(*m):
    print('Analizando os valores passados')
    sleep(1)
    print(f'Foram passados os valores {m} no total de {len(m)} valores')
    sleep(1)
    print (f' O maior valor passado é {max(m)}')        
    

maior(1,2,545,34234,5345664,2342,33)

maior(1,2,3)

maior(1,5345664,2342,33)

maior(1,2,545,3,2342,33)


