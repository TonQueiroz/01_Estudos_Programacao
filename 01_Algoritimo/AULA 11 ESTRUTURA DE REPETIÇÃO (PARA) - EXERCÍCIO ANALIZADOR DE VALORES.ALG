Algoritmo "Analizador de Valores"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 01/03/2023
Var
// Seção de Declarações das variáveis 
C,V,N, SM, DV, NU, SVP : INTEIRO
MD : REAL

Inicio
Escreval("Quantos Valores quer analizar?")
leia (N)
SM <- 0
MD <- 0
DV <- 0
NU <- 0
SVP<- 0


     para C <- 1 ate N passo 1 faça
          Escreval("Digite o Valor a ser analizado?")
          Leia (V)

          SM <- (SM+V)

          MD <- (SM/N)
          
          Se (V%5=0) ENTÃO
             DV <- DV+1
          FIMSE
          
          SE (V=0) ENTAO
             NU<-(NU+1)
          FIMSE
          
          SE (V%2=0) ENTAO
             SVP <- (SVP +V)
          FIMSE
     fimpara

Escreval("A SOMA DE TODOS OS VALORES É ", SM, "." )
Escreval("A MEDIA ENTRE TODOS OS VALORES É ", MD, "." )
Escreval("A QUANTIDADE DE VALORES DIVISIVEIS POR 5 É ", DV, ".")
Escreval("A QUANTIDADE DE NÚMEROS NULOS É  ", NU, "." )
Escreval("A SOMA DE TODOS OS VALORES PARES É ", SVP, "." )
Escreval(" " )
Escreval("OBRIGADO POR UTILIZAR O ANALIZADOR DE VALORES!" )



Fimalgoritmo