Algoritmo "Aula 14 Ordenação de Vetores"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/03/2023
Var
Vet : vetor[1..4] de inteiro
i,j, aux : inteiro

Inicio
para i <-1 ate 4 faça
     escreval(" Digite um Valor: ")
     Leia (Vet[i])
fimpara

para i <-1 ate 3 faça
     para j <- i+1 ate 4 faca
          se (vet[i] > vet[j]) entao
             aux <- vet[i]
             vet[i]<- vet [j]
             vet[j] <- aux
          fimse
     fimpara
fimpara

para i <- 1 ate  4 faca
  escreva ("{", Vet[i], "}")
fimpara


Fimalgoritmo