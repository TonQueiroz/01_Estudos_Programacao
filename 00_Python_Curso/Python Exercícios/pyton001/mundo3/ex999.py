


def teste (num):
    while True:
            
            try:
                num = int(num) 

            except KeyboardInterrupt:
                    
                    print(f'O usuário preferiu não digitar um valor e o valor real foi {num}')
                    
                    input ("valor? ")
            except:
                
                print('Você digitou um dado errado, favor digitar o um número inteiro',end =" ") 
                
                num = str(input('Digite um número...\n'))
            else:
                return num 
            
z = input ("valor?")
x = teste(z)

print (f' o programa  saiu do While sózinho apenas com o return de {x} ')
                          
                

 

        


        


                       
        


