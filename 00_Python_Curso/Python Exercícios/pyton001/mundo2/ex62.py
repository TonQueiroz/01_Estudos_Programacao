'Refaça o desafio de progressão aritimética (61) perguntando se o usuário quer mostrar mais termos! e o programa para quando vc não quer ver mais nenhum termo!!'

pt = int(input('Digite o Primeiro Termo!'))

rz = int(input('Digite a Razão da progressão!'))

tm = int(input('Quantos termos da progressão gostaria de ver ?'))




pa = pt

c = 0

conti = 0 

# exercício meu
'''


while c < tm:

    pa = pa + rz
    print (pa, end ="-")
    c = c+1

    if c == tm:
            
            print(f' O Termo {tm} da progressão aritimética começada em {pt} com razão de {rz} É {pa}!')

            conti = input( 'Você gostaria de Saber mais termos?\n [S] / [N]').upper()

                      
            if conti == "S":
                tmextra = int(input('Quantos termos gostaria de saber a mais ?'))

                

            elif conti=="N":
                print(f' O Termo {tm} da progressão aritimética começada em {pt} com razão de {rz} É {pa}!\n Obrigado por acessar nosso programa')'''

# exercício Proefssor

tmextra = 1
while tmextra != 0:    
    while c < tm:

        pa = pa + rz
        print (pa, end ="-")
        c = c+1
     
    tmextra = int(input( 'Você gostaria de Saber wuantos termoss a mais termos?'))  
    tm = tm + tmextra

print (f'você pediu {c} termos! e o inal foi {pa}')



    