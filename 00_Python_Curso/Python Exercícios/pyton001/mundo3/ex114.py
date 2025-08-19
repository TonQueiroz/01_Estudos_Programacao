# Reescreva a função leiaint() do exercício 104, 
# incluindo agr a possibilidade de  inserção de um número invalido, 
# aproveire e crie tbm uma função leiafloat com a mesma funcionalidade

c = ('\033[m',        # a cor 0 é sem cores
       '\033[37;45m', # a cor 1 é fundo rosa letra branca
       "\33[37;44m",  # a cor 2 é fundo azul letra branca
       '\033[37;41m', # a cor 3 e é fundo vermelho letra branca
       '\33[30;47m'   #  4 fundo branco
       )
#Função para definir se o número é inteiro
def leiaint(num):

    while True:
        print(c[0])
        try:
            num = int(num) 

        except (KeyboardInterrupt, EOFError):
                 print(c[3])
                 print('O usuário preferiu não digitar um valor e o valor real foi {num}')
                 print(c[2])
        
        except:
            print(c[3])
            print('Você digitou um dado errado, favor digitar o um número inteiro',end =" ") 
            print(c[0]) 
            num = str(input('Digite um número...\n'))
                 
        
        else:
            print(c[4])
            print(f'vai retornar o numero {num}', end =" "),
            print(c[0])            
            return num
        

    

#Função para definir se o número é float

def leiafloat(num=0):  
        
        while True:
            print(c[0])
            num = num.replace(',','.')  
            try:
                 num = float(num)

            except (KeyboardInterrupt, EOFError):
                 print(c[3])
                 print('O usuário preferiu não digitar um valor e o valor real foi {num}')
                 print(c[2])

            except:
                 print(c[3])
                 print('Esse dado não pose der float',end =" ")
                 print(c[2])
                 num = input('Digite um dado válido...\n')
                 print(c[0])       


            else:
                print(c[4])
                print(f'vai retornar o numero float {num}', end =" "),
                print(c[0])
                break
        return num
        
#Programa Principal

#chamando a função int

n = str(input('Digite um número inteiro...'))  

respostadafunção = leiaint(n)



print(f'você digitou o valor {respostadafunção}.')

#chamando a função float

n2 = str(input('Digite um número real...'))  

respostadafunção2 = leiafloat(n2)

print(f'você digitou o valor {respostadafunção2}.')