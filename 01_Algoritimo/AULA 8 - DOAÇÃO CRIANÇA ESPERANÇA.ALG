Algoritmo "semnome"
// Disciplina   : [Criança esperança]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 17/02/2023
Var
   // Seção de Declarações das variáveis
   D, VALOR : rEAL

Inicio
   EscrevaL("CRIANÇA ESPERANÇA")
   EscrevaL("oBRIGADO POR DOAR")
   EscrevaL("[1] PARA DOAR R$ 10")
   EscrevaL("[2] PARA DOAR R$ 25")
   EscrevaL("[3] PARA DOAR R$ 50")
   EscrevaL("[4] PARA DOAR R$ 100")
   EscrevaL("[5] PARA ESCOLHER O VALOR")
   EscrevaL("[6] PARA DOAR R$ CANCELAR")

   LEIA (D)

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
   FIMSE


Fimalgoritmo