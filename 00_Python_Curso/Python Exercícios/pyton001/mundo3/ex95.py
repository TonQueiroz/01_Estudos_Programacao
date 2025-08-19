# Aprimore o desafio do jogador de futebol
#Q varios jogadores com sistema de visualização ddos detalhes dos aproveitamentos de cada jogador

#Ver Enunciado
listaaproveitamento = []

apjog={}
golspartidas = []
ccod = cond = 0

while True:
    totalgols = 0
    ccod +=1
    apjog['cod'] = ccod
    apjog['Nome'] = str(input('Nome do jogador?\n'))
    apjog['partidas'] = int(input('Quantas partidas jogou ?\n'))

    for p in range(1,apjog['partidas']+1):
        golspartidas.append(int(input(f'Quantos gols ele fez na partida {p}?\n ')))
        
    for g in golspartidas:
            totalgols += g

    apjog['gols'] = (golspartidas[:])
    apjog['total de gols'] = totalgols

    listaaproveitamento.append(apjog.copy())
    apjog.clear()
    golspartidas.clear()

    saida = " "
    while saida not in "SN":
           saida = str(input('Quer continuar? [S] / [N]')) .upper().strip()[0]

    if saida == 'N':
        saida = " "
        break

print('-='*30)

#print(listaaproveitamento)

print('-='*30)

print (f'{'Codigo':<7}{' Nome':<14}{'Gols':<10}{'Total':<10}')
print('--'*30)

for i in listaaproveitamento:
    print (f'{i['cod']:^7} {i['Nome']:<12} {i['gols'],} {i['total de gols']:>9}')

print('--'*30)
while True:
    while cond > len(listaaproveitamento) or cond == 0:  
        cond = int(input('Digite o código do jogador que gostaria de ver detalhes? [0] para sair\n'))

        if cond > len(listaaproveitamento):
            print('Esse jogador não existe')

        if cond == 000:
            break

    print('--'*30)

    for i in listaaproveitamento:
        
        if cond == i['cod']:
            print(f'LEVANTAMENTO DO JOGADOR\n{i['Nome']}')
            for x,z in enumerate(i['gols']):
                print(f'No jogo {x+1} fez {z} gols')

    saida = " "
    cond = 0
    while saida not in "SN":
           saida = str(input('Quer continuar? [S] / [N]')) .upper().strip()[0]

    if saida == 'N':
        saida = " "
        break

print('Obrigado Por Utilizar Nossos Recursos')
