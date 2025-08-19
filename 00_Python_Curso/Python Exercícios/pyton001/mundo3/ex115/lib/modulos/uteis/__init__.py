def leiaint(num):

    while True:
              
        try:
            num = int(num) 
        
        except:
            
            print('Você digitou um dado errado, favor digitar o certo',end =" ") 
             
            num = str(input('Digite um número...'))
              
        
        else:
            #print(c[4])
            #print(f'vai retornar o numero {num}', end =" "),
            #print(c[0])            
            break
    return num

#Função para definir se o número é float

def leiafloat(num):  
        
        while True:
            num = num.replace(',','.')  
            try:
                 num = float(num)
            except:
                 
                 print('Esse dado não pose der float',end =" ")
                 
                 num = input('Digite um dado válido...')
                 
            else:
                #print(c[4])
                #print(f'vai retornar o numero float {num}', end =" "),
                #print(c[0])
                break
        return num


