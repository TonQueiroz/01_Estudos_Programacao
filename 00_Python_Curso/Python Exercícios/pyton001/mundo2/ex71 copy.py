#CAIXA ELETRÔNICO
#QUAL VALOR SERÁ SACADO NUMERO INTEIRO
# PROGRAMA INFORMARÁ QUANTAS CEDULAS DE CADA SERÁ ENTREGUE DE 50, 20 , 10, 1.

#EXERCÍCIO PROFESSOR!


valor =  int( input('Qual o valor da retirada?'))

total = valor
ced = 50

totced= 0


while True:
      if total >= ced:
            total = total-ced
            totced = totced+1    
     
      else:
            if totced > 0:
                  print(f'{totced} notas de {ced}')
                  totced = 0
            
            if ced == 50:
                  ced = 20
                  
            elif ced == 20:
                  ced = 10
                  
            elif ced == 10:
                  ced = 1
            
            if total == 0 and ced == 1:
                  break
                  
            
      


    
        


      



