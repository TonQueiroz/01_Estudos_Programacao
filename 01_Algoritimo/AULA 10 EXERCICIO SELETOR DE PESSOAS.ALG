Algoritmo "SELETOR DE PESSOAS"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 28/02/2023
Var
 CMC, CFL, SX, CB, ID  : INTEIRO
 R :CARACTERE



Inicio
   ESCREVAL (" BEM VIDO AO SUPER SELETOR DE PESSOAS PARA EMPRESAS")
   
   CMC <- 0
   CFL <- 0

   REPITA

         REPITA
               ESCREVAL (" QUAL O SEXO DO(A) DUNCIONÁRIO(A)? [M]/[F] ")
               ESCREVAL (" MASCULINO      [1] ")
               ESCREVAL (" FEMININO       [2] ")
               LEIA (SX)

                SE (SX<>1) E (SX<>2) ENTAO
                   ESCREVAL ("OPÇÃO INVALIDA, POR FAVOR DIGITE UMA OPÇÃO VALIDA!")
                FIMSE
         ATÉ (SX=1) OU (SX=2)
         
         REPITA
      
               ESCREVAL (" QUAL A COR DO CABELO DO(A) FUNCIONARIO(A)? ")
               ESCREVAL (" PRETO      [1] ")
               ESCREVAL (" LOIRO      [2] ")
               ESCREVAL (" CASTANHO   [3]")
               ESCREVAL (" RUIVO      [4] ")
               LEIA (CB)
      
      SE (CB<>1) E (CB<>2) E (CB<>3) E (CB<>4) ENTAO
                   ESCREVAL ("OPÇÃO INVALIDA, POR FAVOR DIGITE UMA OPÇÃO VALIDA!")
                FIMSE
         ATÉ (CB=1) OU (CB=2)  OU (CB=3) OU (CB=4)
         
         REPITA
               ESCREVAL (" QUAL A IDADE DO(A) FUNCIONARIO(A)? ")
               LEIA (ID)
               
               SE  (ID < 1) E (ID>100) ENTAO
                   ESCREVAL ("OPÇÃO INVALIDA, POR FAVOR DIGITE UMA OPÇÃO VALIDA!")
                FIMSE
         ATÉ (ID>=1) E (ID<=100)
         
         SE (SX=1) E (CB=3) E (ID>=18) ENTÃO
            CMC <- (CMC+1)
         FIMSE
         
         SE (SX=2) E (CB=2) E (ID>=25) E (ID<30) ENTAO
            CFL <- ( CFL + 1)
         fimse
      
      REPITA
         ESCREVAL (" GOSTARIA DE CADASTRAR MAIS OUTRO FUNCIONÁRIO ? [S]/[N]")
         LEIA (R)
         
         SE (R<>"S") E (R<>"N") ENTAO
            ESCREVAL ("OPÇÃO INVALIDA, POR FAVOR DIGITE UMA OPÇÃO VALIDA!")
         FIMSE
         
      ATE (R="S") OU (R="N")
      
   ATÉ  (R="N")
   
   ESCREVAL ("NO PLANTEL DE FUNCIONÁRIOS TEMOS", CMC, " HOMENS DE CABELO CASTANHO E MAIORES DE 18 ANOS.")
   ESCREVAL ("NO PLANTEL DE FUNCIONÁRIOS TEMOS ", CFL, " MULHERES DE CABELO LOIRO  ENTRE DE 25 E 30 ANOS.")
   
   ESCREVAL ("OBRIGADO POR USAR O SELETOR DE FUNCIONÁRIOS.")

Fimalgoritmo