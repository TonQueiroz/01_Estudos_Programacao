#CAIXA ELETRÔNICO
#QUAL VALOR SERÁ SACADO NUMERO INTEIRO
# PROGRAMA INFORMARÁ QUANTAS CEDULAS DE CADA SERÁ ENTREGUE DE 50, 20 , 10, 1.



while True:
      saque = int(input('Qual será o valor do saque?'))

      cinq = saque//50

      saque = saque -(cinq*50)

      vint = saque //20

      saque = saque - (vint*20)

      dez = saque // 10

      saque = saque - (dez*10)

      um = saque//1

      print(f'''
      Notas de 50 = {cinq}

      Notas de 20 = {vint}

      Notas de 10 = {dez}

      Notas de 1 = {um}
            ''')
      while True:
            saida=str(input('gostaria de fazer outro saque ?')).upper().strip()[0]
            if saida in "SN":
                  break
      if saida in "N:":
            break

print ('obrigado por usar nosso banco!')



      



