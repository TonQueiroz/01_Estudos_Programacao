#Ler varios numeros e colocar numa lista 
#2 listas extreas com valores pares e impares
#mostre as 3 listas geradas




#Digite uma expressão numérica pada dizer se  é válida. 
#((a+b)*a) = x
c1= c2 = c3 =0

expressão = str(input('digite a expressão'))


for l in expressão:
        if l == "(":
                c1+=1
        elif l==")":
                c2+=1
        elif l == "=":
                c3+=1

if c2 == c1 and c3 ==1:
        print('Essa expressão numérica é válida!')
else:
        print('Essa expressão numérica NÃO é válida!') # A minha ficou errada se eu colocas parenteses ao contrário ela da como válida

#Exercício professor
pilha= []

for l in expressão:
        if l =="(":
                pilha.append(l)
        elif l ==")":
                if len(pilha) >0:
                        pilha.pop()
                else:
                        pilha.append(')')
if len(pilha) == 0:
        print('Essa expressão numérica é válida!')
else:
        print('Essa expressão numérica NÃO é válida!')
