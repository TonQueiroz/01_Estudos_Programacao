Algoritmo " NUMERO FATORIAL?"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 24/02/2023
Var
   // Seção de Declarações das variáveis

   C, N, F   : INTEIRO
   R : CARACTERE



Inicio
   REPITA
      ESCREVAL (" QUER SABER O FATORIAL SE QUAL NÚMERO ? " )
      LEIA (N)
      F <- 1
      REPITA
         ESCREVA (N, " X " )
         F <- F * N
         N<- (N-1)
      ATÉ (N < 1)

      ESCREVAL (" O NÚMERI FATORIAL DE  ", N, " É ", F)

      ESCREVAL (" GOSTARIA DE SABER O FATORIAL DE OUTRO NUMERO ? [S]/[N]")
      LEIA (R)
      LIMPATELA
   ATE (R = "N")

   ESCREVA (" OBRIGADO POR USAR O APFAT.")





Fimalgoritmo