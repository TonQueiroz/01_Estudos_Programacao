''' bases numéricad
CONVERTA O VALOR PARA 1-bINARIO 2-OCTAL 3-HEXADECIMAL'''

n1 = int(input('''Qual número deseja transformar?'''))

cond = int(input('''gostaria de transformalo em
               [1] - BINARIO 
               [2] - OCTAL 
               [3] - HEXADECIMAL?'''))


if cond == 1:
    print(f' o número {n1} em número BINÁRIO é {bin(n1)[2:]} ')

elif cond == 2:
    print(f''' o número {n1} em número OCTAGONAL é {oct(n1)[2:]}''')

elif cond == 3:
    print(f''' o número {n1} em número HEXADECIMAL é {hex(n1)[2:]}''')

else:
    print('entrada inválida')

