#Tabuada de varios número umd e cada vez E pare quando o número solicitado for negativo




while True:
    n = int(input('Qual numero deseja saber a tabuada?'))
    
    if n < 0 :
        break

    for c in range(0,10+1):
        print (f'{n} x {c} = {n*c}' )

    
