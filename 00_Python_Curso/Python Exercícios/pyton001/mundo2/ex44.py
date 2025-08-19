''' EXERCÍCIO 44 ---

ELABORE UM PROGRAMA QUE CALCULE O VALOR POR UM PRODUTO CONSEDERANDO SEU PREÇO NORMOAL E CONDIÇÃO DE PAGAMENTO

A VISTA 10% DESCONTO

A VISTA CARTÃO 5%

EM 2 VEZES PREÇO NORMAL

3 X OU MAIS 20% DE JUROS'''

preço = 1000.00

cond = int(input('''Qual a condição de pagamento? 
                 
[1] A VISTA DINHEIRO 
                 
[2] A VISTA CARTÃO 
                 
[3] EM 2 VEZES 
                 
[4] 3 X OU MAIS?''' ))

print (f'NESSA CONSIÇAO DE PAGAMENTO O PRODUTO SAIRÁ')

if cond == 1:
    print (f'{preço*0.9}')

elif cond==2 :
    print(preço*0.95)

elif cond == 3:
    print(preço)

elif cond == 4:
    print(preço*1.2)

else:
    print (f'condição inválida')

