#Ler nome e peso de várias pessoas e guarde tudo em uma lista
# A ) Quantas pessoas foram cadastradas?
#B) Lista com as mais pesadas
#C) Lista com as mais leves


listapp = []
listatemporária = []
menorpeso=[]
maiorpeso=[]


cont = maxp= minp= 0




while True:
        listatemporária.append(str(input('Nome?')))
        listatemporária.append(int(input("Peso?")))
        listapp.append(listatemporária[:])
        listatemporária.clear()

        cont+=1

        saida = " "
        while saida not in'SN':
                saida = str(input('Quer continuar?')).upper().strip()[0]

        if saida in "N":
                break

for c in listapp :
        print(c)
        if c[1] > maxp:
                maxp=c[1]
                maiorpeso = [c[:]]
        elif maiorpeso[0][1] == c[1]:
                maiorpeso.append(c[:])        
                

        if c[1] < minp or minp==0:
                minp=c[1]
                menorpeso= [c[:]]
        elif menorpeso[0][1] == c[1]:
                menorpeso.append(c[:])
        
print (f'Quantidade de pessoas cadastradas foram {cont} \n Menor peso {menorpeso} kg \n maior peso {maiorpeso} com !')

