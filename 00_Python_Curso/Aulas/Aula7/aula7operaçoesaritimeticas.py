print ('oi'*2)

n1=int(input("Primeiro Valor?"))
n2 = int(input('segundo Valor?'))

so=n1+n2
su=n1-n2
m=n1*n2
exp=n1**n2
d=n1/n2
dint=n1//n2
rest=n1%n2



print('A soma de {} e {} é = {}'.format(n1, n2, so))

print('A Subtração de {} e {} é = {}'.format(n1, n2, su))

print('A Multiplicação de {} e {} é = {}'.format(n1, n2, m))

print('o numero {} elevado a {} é = {}'.format(n1, n2, exp))

print('A divisão de {} com {} é  = {}'.format(n1, n2, d))

print('A divisão inteira de {} com {} é = {:>15} !'.format(n1, n2, dint), end=""  )

print('O resto da Divisão de {} com {} \n  é {}'.format(n1, n2, rest))