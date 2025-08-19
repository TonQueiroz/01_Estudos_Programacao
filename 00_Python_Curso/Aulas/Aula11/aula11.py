#Cores em Python no Terminal com ANSI

''' 
Codigo de Estilos e cores

Estilos

0 == none
1 == Negrito
4 == Sublinhado
7== Invertido (Troca a Cor do Fundo e da Letre)

Cores letras

30 == Branco
31 == Vermelho
32 == Verde
33  == Amarelo
34 == Azul
35 == Magenta
36 == Ciano
37 == Cinza

Cores fundo

40 == Branco
41 == Vermelho
42 == Verde
43  == Amarelo
44 == Azul
45 == Magenta
46 == Ciano
47 == Cinza

Linha de Comando ANSI Escape Sequense ---> /033[4;33;44m

Para voltar as configurações originais e para fechar parar as formatações na linha --> /033[m

'''

print('\033[4;35;46m olá  \033[m Mundo ') 