Algoritmo "sUPER CONTADOR"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 27/02/2023
Var
   CPR, R : CARACTERE
   CONTADOR : INTEIRO

procedimento PGR ()
inicio
   CONTADOR <- 1
   REPITA
      ESCREVA (CONTADOR, "..., ")
      CONTADOR <- (CONTADOR +1)
   ATÉ (CONTADOR > 10)
   ESCREVAL(" ")

fimprocedimento

procedimento RGR
inicio
   CONTADOR <- 10
   REPITA
      ESCREVA (CONTADOR, "..., ")
      CONTADOR <- (CONTADOR -1)
   ATÉ (CONTADOR < 1)
   ESCREVAL(" ")


fimprocedimento

procedimento ERR
inicio
   ESCREVAL ("OPÇÃO INVALIDA, POR FAVOR DIGITE UMA OPÇÃO VALIDA!")

fimprocedimento




Inicio


   ESCREVAL (" BEM VIDO AO SUPER CONTADOR ")
   REPITA
      REPITA
         ESCREVAL (" SE VOCÊ QUER CONTAR DE 1 A 10 DIGITE [A] ")
         ESCREVAL (" SE VOCÊ QUER CONTAR DE 10 A 1 DIGITE [B] ")
         LEIA (CPR)
         SE (CPR <> "A") E (CPR <> "B")ENTÃO
            LIMPATELA
            ERR
         FIMSE
      ATE (CPR = "A") OU (CPR = "B")

      SE (CPR = "A") ENTÃO
         PGR

      SENÃO FIMSE
         SE (CPR = "B") ENTÃO
            RGR
         fimse
      FIMSE

      REPITA
         ESCREVAL (" GOSTARIA DE CONTAR NOVAMENTE? [S]/[N] ")
         LEIA (R)
         SE (R<>"N") E (R<>"S") ENTAO
            ERR
         FIMSE
      ATE (R="N") OU (R="S")
   ATE (R="N")
   ESCREVAL ("-- OBRIGADO POR UTILIZAR O SUPERCONTADOR! --")

Fimalgoritmo