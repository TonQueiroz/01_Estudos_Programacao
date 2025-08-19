#Achando sen, cos, e tang do angulo com import da biblioteca math

import math

Ang = int(input('Digitte o Angulo Desejado?'))

cos = math.cos( math.radians(Ang) )
sen = math.sin(math.radians(Ang))
tan = math.tan(math.radians(Ang))

print('O Coseno do angulo é {} \n o seno do angulo é {} \n e a tangente do angulo é {}'.format(cos, sen, tan))

