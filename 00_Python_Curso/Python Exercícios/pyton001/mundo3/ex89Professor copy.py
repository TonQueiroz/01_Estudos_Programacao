#leia nome e 2 notas em uma lista composta com a lista de alunos, lista de nomes e lista de notas 3 listas uma dentro da outra
#mostre um boletim contendo as médias de cada um
#permita que o usuário possa mostrar as notas de cada aluno individualmente


listageral2= []
          
#"Ana: 8.5, 9.0", "Lucas: 7.0, 6.5", "Mariana: 9.5, 8.8", "Pedro: 6.0, 7.2", "Sofia: 8.0, 7.5"

while True:
        nome = str(input('Nome Aluno?'))
        nota1 = float(input('Nota Português'))
        nota2 = float(input('Nota Matemática?'))

        média= ((nota1+nota2)/2)

        listageral2.append([nome, [nota1,nota2],média])

            
        print(listageral2)

        saida = " "
        while saida not in 'SN':
                saida = input('Quer cadastrar mais um aluno? [S]/[N]').upper().strip()[0]    

        if saida in "N":
                break

print ("=-"*30)
print( f'{'BOLETIN:':^60}')
print ("=-"*30)

for i, item in enumerate(listageral2):
        print(f'Aluno {i} - {f'Nome{item[0]}':>5} {f'Média = {item[2]}':.>30}')


escolha = int(input('Gostaria de Ver as notas de qual aluno?'))
for i, item in enumerate(listageral2):
        if escolha == i:
                print(f'As notas do aluno {i} {item[0]} foram \n Português {item[1][0]} Matemática {item[1][1]} Média = {item[2]}')













    















