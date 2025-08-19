'''LEIA A PESO DE 5 PESSOAS E ME CONTE QUAL FOI O MAIOR E MENOR PESO'''
maiorpeso = 0
for c in range(1,5+1):
    peso = int(input(f'Qual o peso da {c}ª Pessoa?'))
    if peso > maiorpeso:
        maiorpeso = peso

print (f'o maior peso é {maiorpeso}')