Algoritmo "Turma"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/03/2023
Var
nome : vetor[1..4] de caractere
N1 : vetor [1..4] de real
N2 : vetor [1..4] de real
m : vetor [1..4] de real
n, Q : inteiro

Inicio
       escreval ("LISTAGEM DE TURMA")
       escreval ("quantos alunos gostaria de listar?")
       Leia (Q)
       
       para n<-1 ate Q faca
         escreval ("Qual o  nome do " ,n, "o aluno?")
         leia (Nome[n])
         
         escreval ("Qual a 1a nota do aluno?", nome[n])
         leia (N1[n])
         
         escreval ("Qual a 2a nota do aluno?", nome[n])
         leia (N2[n])
         
         m[n] <- ((N1[n]+N2[n])/2)
         
         n<- (n+1)
       fimpara
       
       para n<-1 ate Q faca
       
       Escreval ("- O " ,n," o aluno ",nome[n], " Teve notas " ,N1[n], " e " ,N2[n]," então teve média " ,m[n])
       
       n<- (n+1)
       
       fimpara
       
       escreval ("Obrigado por usar a listagem automática!")

Fimalgoritmo