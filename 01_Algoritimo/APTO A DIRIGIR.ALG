Algoritmo "APTO A DIRIGIR?"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : CURSO EM VÍDEO
// Descrição   : INFORMA SE O USUÁRIO ESTA APTO A DIRIGIR
// Autor(a)    : TONQUEIROZ
// Data atual  : 17/02/2023
Var
// Seção de Declarações das variáveis 
 ANIV, NM, HB, VL                     : CARACTERE

  AN, AA, IDADE, PTS           : INTEIRO


Inicio
      ESCREVAL ("OLÁ")
      ESCREVAL ("QUAL SEU NOME?")
      LEIA (NM)
      
      ESCREVAL ("EM QUE ANO NASCEU?")
      LEIA (AN)
      
      ESCREVAL ("EM QUE ANO ESTAMOS?")
      LEIA (AA)

      ESCREVAL ("JÁ FEZ ANIVERSÁRIO ESSE ANO? [S/N]")
      LEIA (ANIV)
      
      SE (ANIV <> "S") ENTÃO
         IDADE <- (AA-AN-1)
         SENÃO
         IDADE <- (AA-AN)
      FIMSE
      
      ESCREVAL (" VOCÊ TEM ", IDADE, " ANOS DE IDADE.")
      
      SE (IDADE < 18) ENTÃO
                ESCREVAL (" VOCÊ AINDA NÃO TEM IDADE O SUFICENTE PARA DIRIGIR")
         SENÃO
                ESCREVAL ("JÁ RETIROU SUA HABILITAÇÃO? [S/N]")
                LEIA (HB)
                     SE (HB <> "S") ENTÃO
                        ESCREVAL (" VOCÊ AINDA NÃO PERMISSÃO DIRIGIR POIS NÃO RETIIROU SUA HABILITAÇÃO")
                     SENAO
                          SE(HB="S") ENTAO
                                      ESCREVAL ("SUA HABILITAÇÃO ESTÁ DENTRO DO PRAZO DE VALIDADE? [S/N]")
                                      LEIA (VL)
                                           SE (VL <> "S") ENTÃO
                                              ESCREVAL (" VOCÊ NÃO TEM PERMISSÃO DIRIGIR POIS SUA HABILITAÇÃO ENTÁ FORA DO PRAZO DE VALIDADE")
                                           SENAO
                                                SE (VL="S") ENTÃO
                                                   ESCREVAL (" QUANTOS PONTOS VOCÊ TOMOU EM MULTAS? ")
                                                   LEIA (PTS)
                                                        SE (PTS < 20) ENTÃO
                                                           ESCREVAL ("VOCÊ ESTÁ APTO A DIRIGIR")
                                                        SENÃO
                                                           ESCREVAL ("VOCÊ NÃO ESTÁ APTO A DIRIGIR POIS TOMOU MUITOS PONTOS NA CARTEIRA")
                                                        FIMSE
                                                FIMSE
                                           FIMSE
                          FIMSE
                     FIMSE
         FIMSE
      Fimalgoritmo