#Crie uma matriz 3x3 e preencha os números com valores lidos, no final mostre a matriz na tela com a formatação correta

Matriz = []

linha = []
for l in range (0,3):
        for n in range(0,3):
                n = int(input(f'Digito número da posição [{l},{n}] '))
                linha.append(n)
        Matriz.append(linha[:])
        linha.clear()

print('=-'*30)

for p  in range(0,3):
        
        for q in range(0,3):
                print(f'[{Matriz[p][q]:^5}]', end=" ")
        
        print('')



    















