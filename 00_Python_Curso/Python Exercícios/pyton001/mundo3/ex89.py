#leia nome e 2 notas em uma lista composta com a lista de alunos, lista de nomes e lista de notas 3 listas uma dentro da outra
#mostre um boletim contendo as médias de cada um
#permita que o usuário possa mostrar as notas de cada aluno individualmente


listageral= []
listalunos = []
listanotas=[]
listageral2= []
          
#"Ana: 8.5, 9.0", "Lucas: 7.0, 6.5", "Mariana: 9.5, 8.8", "Pedro: 6.0, 7.2", "Sofia: 8.0, 7.5"

while True:
        nome = str(input('Nome Aluno?'))
        nota1 = float(input('Nota Português'))
        nota2 = float(input('Nota Matemática?'))

        média= ((nota1+nota2)/2)


        dados= [nome, [nota1,nota2],média]

        listageral2.append(dados[:])

        listalunos.append(nome)
        listanotas.append(nota1)
        listanotas.append(nota2)

        listalunos.append(listanotas[:])

        listanotas.clear()

        listageral.append(listalunos[:])

        listalunos.clear()

        print (listageral)


        saida = " "
        while saida not in 'SN':
                saida = input('Quer cadastrar mais um aluno? [S]/[N]').upper().strip()[0]    

        if saida in "N":
                break

print ("=-"*30)
print( f'{'BOLETIN:':^60}')
print ("=-"*30)



for i, c in  enumerate(listageral):
     

        nome = c[0]

        nota = c[1]

        notap = nota[0]

        notam = nota[1]

        print(f'Aluno  {nome:.<20} Port. = {notap:<5}  _ Mat. = {notam :<5} _ MÉDIA = {(notam+notap)/2:<10.2F}')

        

      
notaespecífica  = str(input('quer saber a nota de qual aluno?'))
for i, c in  enumerate(listageral):  
        nome = c[0]

        nota = c[1]

        notap = nota[0]

        notam = nota[1]

        if notaespecífica in c:
                print(f'Aluno  {nome:.<20} Port. = {notap:<5}  _ Mat. = {notam :<5} _ MÉDIA = {(notam+notap)/2:<10.2F}')       
            
        













    















