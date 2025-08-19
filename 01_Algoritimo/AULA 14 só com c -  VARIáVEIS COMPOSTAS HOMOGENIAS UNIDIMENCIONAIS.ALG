Algoritmo "SoComC"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/03/2023
Var
Nome: Caractere
SoC : vetor[1..10] de Caractere
c, QN, tot : inteiro


Inicio
 Escreval ("Qual a quantidade de Nomes que deseja analizar?" )
 leia (QN)

 para c<-1 ate QN faca
      escreval(" digite o nome ")
      leia (nome)
      Se (copia(maiusc(nome),1,1) = "C") então
      tot<- (tot+1)
      SoC[tot] <- nome
      fimse
 fimpara
 limpatela
 
    Escreval ("Listagem Final")
     para c<-1 ate tot faca
     Escreval (" A quantidade de nomes começados com a Letra C são" ,Soc[c])

     fimpara


Fimalgoritmo

