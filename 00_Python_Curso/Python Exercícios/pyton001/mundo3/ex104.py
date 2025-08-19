# Função chamda leiaint
# vai funcionar como um input, vai fazer a validação pra aceitar apenas um valor numérico

def leiaint():
    while True:      
        ok = False
        num = str(input('Digite um número...'))

        if num.isnumeric():
            num = int (num)
            ok = True           
        
        else:
            
            print('\33[037;41m Você não digitou um número \33[0m')
        
        if ok:
            break
        
    return num


respostadafunção = leiaint()

print(f'você digitou o valor {respostadafunção}.')


    
    



