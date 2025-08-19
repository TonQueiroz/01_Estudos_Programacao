Algoritmo "semnome"
// Disciplina   : [Criança esperança]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 17/02/2023
Var
   // Seção de Declarações das variáveis
   R, DC, XXX : INTEIRO

procedimento Doacao(VAR TD : REAL)
var
   D, VALOR : REAL
   C, CONT, F : INTEIRO

inicio
   F<- 5
   EscrevaL("VAMOS LÁ")
   REPITA
      EscrevaL("[1] PARA DOAR R$ 10")
      EscrevaL("[2] PARA DOAR R$ 25")
      EscrevaL("[3] PARA DOAR R$ 50")
      EscrevaL("[4] PARA DOAR R$ 100")
      EscrevaL("[5] PARA ESCOLHER O VALOR")
      EscrevaL("[6] PARA DOAR R$ CANCELAR")

      LEIA (D)

      SE (D <> 1) E (D <> 2) E (D <> 3) E (D <> 4) E (D <> 5) E (D <> 6) ENTAO

         ESCREVAL ("OPÇÃO INVALIDA POR FAVOR ESCOLHA UMA OPÇÃO VALIDA")

      FIMSE


ATE (D = 1) OU (D = 2) OU (D = 3) OU (D = 4) OU (D = 5) OU (D = 6)

ESCOLHA D
CASO 1
   VALOR <- 10

CASO 2
   VALOR <- 25

CASO 3
   VALOR <- 50

CASO 4
   VALOR <-100

CASO 5
   EscrevaL("ESCOLHA O VALOR DA DOAÇÃO")
   Leia (Valor)

CASO 6
   eSCREVAl ("SUA DOAÇÃO NÃO FOI EFETUADA, OBRIGADO PELO CONTATO")

FIMESCOLHA
SE (D = 1) OU (D = 2) OU (D = 3) OU (D = 4) OU (D = 5)  ENTÃO
   EscrevaL ("OBRIGADO POR DOAR R$ ", VALOR, ".")
   TD <- TD + VALOR
FIMSE

fimprocedimento

PROCEDIMENTO ERRO()
INICIO
   EscrevaL(" OPÇÃO INVALIDA, ESCOLHA A OPÇÃO CERTA PARA CONTINUAR...")

FIMPROCEDIMENTO
Inicio

   EscrevaL("BEM  VINDO A DOAÇÃO DO CRIANÇA ESPERANÇA")

   REPITA
      EscrevaL("GOSTARIA DE FAZER UMA DOAÇÃO? [1]SIM  [2]NAO")
      LEIA (DC)

      SE (DC<>1) E (DC<>2) ENTÃO
         ERRO()
      SENAO
         SE  (DC=1) ENTÃO
            DOACAO (XXX)
         SENÃO
            SE (DC=2) ENTAO
               EscrevaL("TERMINAMOS AQUI ENTÃO MÃO DE VACA, OBRIGADO PELO SEU CONTATO!")
            FIMSE
         FIMSE
      FIMSE
   ATE (DC = 1) OU (DC = 2)

   SE (DC = 1)  ENTAO
      REPITA
         EscrevaL("DESEJA FAZER OUTRA DOAÇÃO? [1]SIM [2]NÃO")
         LEIA (R)

         SE (R<>1) E (R<>2) ENTÃO
            ERRO ()
         SENAO
            SE  (R=1) ENTÃO
               DOACAO (XXX)
            SENÃO
               SE (R=2) ENTAO
                  EscrevaL("OBRIGADO PELA DOAÇÃO TOTAL DE",XXX," REAIS!")
               FIMSE
            FIMSE
         FIMSE
      ATE (R = 2)
   FIMSE



Fimalgoritmo