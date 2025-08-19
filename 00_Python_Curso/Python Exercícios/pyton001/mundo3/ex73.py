#Tupla com a tabela do brasileirão
#apenas os 5 primeiro colocados
# Os ultimos 4 colocados
#Lista com os times em ordem alfabética
# Em que posição está o time do são paulo

classificação = ("Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional", "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco", "Vitória", "Atlético-MG", "Fluminense", "Grêmio", "Juventude", "Bragantino", "Santos", "Mirassol", "Sport", "Ceará")

print ('-=' *30)

print ( 'os 5 primeiro colocados são\n', classificação[:5])
print ('-=' *30)
print( 'Os 4 ultimos são\n',classificação[-4:])
print ('-=' *30)
print('Os times em ordem alfabética\n',sorted(classificação))
print ('-=' *30)
print (f'O São Paulo esta na {classificação.index('São Paulo')+1}ª colocação!',)