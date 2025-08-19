'Crie um programa que leia dois valores e mostra um menu na tela soma, multiplicar, maior, novos numeros ou sair do programa.'



cond = 4

while cond != 9:
    if cond == 4:
        V1 = int(input('Digite o primeiro Valor?'))

        V2 = int(input('Digite o Segudo Valor?'))

    cond = int(input('O que você deseja fazer com os números \n [1] Somar [2] Multiplicar [3] Mostrar o maior [4] Escolher nóvos numeros [9] Sair'))

    if cond == 1 :
        print(f'{V1 +V2} É a soma de  {V1} + {V2}.')
    
    elif cond == 2:
        print(f'{V1*V2} É a soma de  {V1} + {V2}.')
    
    elif cond == 3:
        VM = V1
        if V1 < V2:
            VM = V2
        print(f'{VM} É o maior númeor.')

    elif cond == 9 :
        print('Obrigado até a próxima!')
    
    else:
        print('Opção inválida tennte novamente!')

