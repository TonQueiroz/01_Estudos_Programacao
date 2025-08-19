#Aula 23 Tratamento de Erros e Excessões


#TRY EXCETP ELSE FINALLY


'''try:
    a= int(input('n1'))
    b= int(input('n1'))
    c = a/b
except :
    print('Deu erro aí cuzao')

else:
    print(f'O redultado é {c}')

#Exceções definindo o tipo de  exception como variavel 
try:
    a= int(input('n1'))
    b= int(input('n1'))
    c = a/b
except Exception as erro:
    print(f'Deu erro aí cuzao {erro.__class__}')

else:
    print(f'O redultado é {c}')'''


#Exceções com  mais de um except designando respostas para erros específicos

try:
    a= int(input('n1'))
    b= int(input('n1'))
    c = a/b
except (ValueError, TypeError):
    print(f'erro de tipo de dado, não ta vendo não?')

except (ZeroDivisionError):
    print(f'Não da pra dividir por 0 burro!{ZeroDivisionError}')

except:
    print(f'Só deu erro, cuidado aí é esse aqui,{Exception.__class__} se vira ')

else:
    print(f'O redultado é {c}')