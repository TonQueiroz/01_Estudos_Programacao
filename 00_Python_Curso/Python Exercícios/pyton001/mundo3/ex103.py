# Função chamda ficha
# recebe 2 parametros nome do jogador e quantos gols ele marcou
#o programa deverá ser capaz de mostrar a ficha do jogador mesmos e nao tenha sido informado algum dado corretamente


def ficha(nome='Unknow', gols=0):
    gols= (int(gols))
    r = f'O jogador {nome} fez {gols} gols no campeonato.'
    return r


jogador = str(input('Qual o nome do jogador?'))
aproveitamento = str(input('Quantos gols ele fez no campeonato?'))

# para verificar se a string digitada pode ser numerica
if aproveitamento.isnumeric():
    aproveitamento =int(aproveitamento)
else:
    aproveitamento = 0

if jogador.strip() == "":
    resp =ficha(gols=aproveitamento)
else:
    resp =ficha(jogador,aproveitamento)

print(resp)


            


    


    
    



