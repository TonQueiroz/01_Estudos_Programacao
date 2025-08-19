Algoritmo "MELHOR ALUNO DA SALA ?"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 23/02/2023
Var
// Seção de Declarações das variáveis
 QA, CONT : INTEIRO
 NT,NM : REAL
NA, NAF : CARACTERE
Inicio
      EscrevaL ("QUANTOS ALUNOS TEM NA SALA??")
        LEia (QA)
        Cont <- 1

                       enquanto (Cont <= QA) faça

                           Escreval ("NOME DO ALUNO?")
                           LEIA (NA)
                           ESCREVAL  ("QUAL A NOTA DO " ,NA,"?")
                           LEIA (NT)
                                    SE (NT > NM) ENTÃO
                                    NM<- NT
                                    NAF <- NA
                           FIMSE
                           
                           CONT <- (cONT+1)
                       fimenquanto
                       
                       Escreval ("O MELHOR ALUNO DA SALA FOI ", NAF, " SUA NOTA FOI ", NM, "." )





Fimalgoritmo