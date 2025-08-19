#Aula 19 Dicionários
'''
pessoas = { 'nome': 'Cleiton',  'Sexo':'M', 'Idade': 33}
print(f' Valores, { pessoas.values()}')
print(f' Chaves , {pessoas.keys()}')
print(f' Itens , {pessoas.items()}')


print (f'O {pessoas['nome']}, tem {pessoas['Idade']} anos')

for v in pessoas.values():
    print(v)


for k in pessoas.keys():
    print(k)


for k,v in pessoas.items(): #Esse no lugar do enumearate
    print(k,v)

del pessoas['Sexo'] #Esclui a chave e valor de sexo

print (pessoas)

pessoas['peso'] = 85 #adiciona assim chave e valor

print(pessoas)
'''
#Dicionario dentro de uma lista

'''estado1 = { 'uf' : 'Rio de Janeiro' , 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'Sigla':'SP'}

Brasil=[]

Brasil.append(estado1)
Brasil.append(estado2)

print(estado1)
print(estado2)

print(Brasil) #[{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'Sigla': 'SP'}]

print(Brasil[0]['uf'])'''

estado = dict() # ou {} Dicionario

brasil2 = list() #Lista

for c in range(0,3):
    estado['uf'] = str(input('Estado?'))    
    estado['Sigla'] = str(input('Sigla?'))
    brasil2.append(estado.copy()) #Metodo copy para copiar e não referir um dicionário ao outro pois referindo muda sempre que colocar na lista

print(brasil2) #[{'uf': 'S]ão paulo', 'Sigla': 'sp'}, {'uf': 'Roraima', 'Sigla': 'RO'}, {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}]

for e in brasil2:
    for k, v in e.items():
        print(f'chave {k} valor {v}')

print('-='*30) 

for e in brasil2:
    for v in e.values():
        print(f'valor {v}')


