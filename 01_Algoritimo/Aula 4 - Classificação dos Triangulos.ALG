Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 15/02/2023
Var
L1, L2, L3 : Inteiro
EQ, ES, Tri : Logico


Inicio
EscrevaL ("Informe o primeiro Lado do triangulo")
Leia (L1)
EscrevaL ("Informe o Segundo Lado do triangulo")
Leia (L2)
EscrevaL ("Informe o Terceito Lado do triangulo")
Leia (L3)
Tri <- (L1<L2+L3) e (L2<L1+L3) e (L3<L1+L2)
Escreval ("Essas medidas podem formar um Triangulo ?", TRI)
EQ <- (L1=L2) e (L2=L3)
Escreval ("Esse triangulo é Eqilatero ?", EQ)
Es <- (L1<>L2) e (L2<>L3) e (L3<>L1)
Escreval ("Esse triangulo é Edcaleno ?", Es)
Tri <- (L1<L2+L3) e (L2<L1+L3) e (L3<L1+L2)
Escreval ("Essas medidas podem formar um Triangulo ?", TRI)

Fimalgoritmo