'Faça um programa que leia o sexo de uma pessoa e só aceite  M ou F, Caso esteja errado peça a digitação novamente até ter um valor correto'

sexo =  input('Qual o seu sexo ?[M] / [F]').upper()[0].strip()

while sexo not in "MF":
    sexo = str(input('Digite uma  entrada válida! Qual o sexo?')).upper()
         
print(f'O Sexo cadastrado foi {sexo}!')

