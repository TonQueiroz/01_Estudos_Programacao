Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Curso em vídeo
// Descrição   : Determinar a nota de um aluno atraves da Pontuação
// Autor(a)    : TonQueiroz
// Data atual  : 21/02/2023
Var
   NOME, NTF : CARACTERE
   NP, NM, MD : REAL



Inicio
   Escreval ("--------------------------")
   Escreval ("Bem vindo a área do aluno")
   Escreval ("--------------------------")
   Escreval ("Qual o seu nome aluno?")
   Leia (Nome)
   Escreval ("Qual sua nota de português")
   Leia (NP)
   Escreval ("Qual sua nota de Matemática?")
   Leia (NM)

   MD <-((NP+NM)/2)
   SE (NP <0) OU (NP >10) OU (NM<0) OU (NM >10) ENTAO
      ESCREVAL ("NOTAS INVÁLIDAS, TENTE NOVAMENTE E INSIRA NOTAS VALIDAS PARA PODERMOS CONTINUAR.")
   SENÃO
      Se (MD >=9) e (MD<=10)Então
         NTF <-("A")
      senão
         se (MD >=8) e (MD<9)Então
            NTF <- ("B")
         Senão
            se (MD >=7) e (MD<8)Então
               NTF <- ("C")
            Senao
               se (MD >=6) e (MD<7)Então
                  NTF <- ("D")
               senao
                  se (MD >=5) e (MD<6)Então
                     NTF <- ("E")
                  senao
                     se (MD <5) E (MD>=0) Então
                        NTF <- ("F")
                     FIMSE
                  fimse
               fimse
            fimse
         fimse
      fimse

      Se (NTF = "A") OU (NTF ="B") OU (NTF ="C") ENTAO
         Escreval ("Sua Media final foi ", NTF, ("."))
         ESCREVAL ("PARABENS ",NOME, "! VOCÊ FOI APROVADO!")
      SENAO
         SE (NTF = "D") OU (NTF ="E") OU (NTF ="F") ENTAO
            Escreval ("Sua Media final foi ", NTF, ("."))
            ESCREVAL ("SINTO MUITO! VOCÊ FOI REPROVADO!")
         fimse
      FIMSE
   FIMSE

Fimalgoritmo