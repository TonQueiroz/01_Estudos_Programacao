Algoritmo "Contagem inteligente"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 23/02/2023
Var
// Seção de Declarações das variáveis
N1, N2, cont : inteiro

Inicio
      EscrevaL ("De Qual numero a Qual numer gostaria de contar?")
               Escreva ("1º Número? ")
               LEia (N1)
               
               Escreva ("2º Número? ")
               LEia (N2)
               
               Se (N1>N2) Então
                  Cont <- N1

                       enquanto (Cont >= N2) faça
                           Escreval (cont)
                           Cont <- (Cont - 1)
                       fimenquanto
               Senao
                  Cont <- N1

                       enquanto (Cont <= N2) faça
                           Escreval (cont)
                           Cont <- (Cont +1)
                       fimenquanto
                  fimse
               Escreval ("fim de contagem")


Fimalgoritmo