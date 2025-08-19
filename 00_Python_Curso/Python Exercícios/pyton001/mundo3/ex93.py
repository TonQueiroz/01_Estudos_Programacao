#Gerencie o aproveitamento de um jogador de futebol
#Nome do Jogadior , quantas partidas ele jogou, quantidade de gols feitos em cada partida 
#guarde tudo em u dicionário, uncluindo o total de gols feitos durante o campeonato.

#Ver vídeo no enunciado tem coisa a mais


apjog={}
golspartidas = []
totalgols = 0


apjog['Nome'] = str(input('Nome do jogador?\n'))
apjog['partidas'] = int(input('Quantas partidas jogou ?\n'))

for p in range(1,apjog['partidas']+1):
    golspartidas.append(int(input(f'Quantos gols ele fez na partida {p}?\n ')))
    
'''for g in golspartidas:# Essa parte  era meu código
        totalgols += g''' #1 Essa parte  era meu código

apjog['gols'] = (golspartidas[:])
apjog['totalgols'] = sum(golspartidas)
'''apjog['total de gols'] = totalgols #  Essa parte  era meu código'''#1 Essa parte  era meu código

apjog['total de gols'] = sum(golspartidas) #1 Código igual do Professor mais prárico

print('-='*30)

print(apjog)

print('-='*30)

for k, i in apjog.items():
      
      print(f'O campo {k} tem o valor -> {i}.' )


print('-='*30)
print(f' O Jogador{apjog['Nome']} jogou {apjog["partidas"]} partidas')
for a,s in enumerate (golspartidas):
      print(f' Na partida {a+1}, fez {s} gols')

print(f' Foi um total de {apjog['total de gols']}.')
      
