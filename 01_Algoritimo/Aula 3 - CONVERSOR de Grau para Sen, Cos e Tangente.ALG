Algoritmo "Conversor"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 15/02/2023
Var
// Seção de Declarações das variáveis 
      Angulo, S, C, T: Real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
                            Escreva  ("Informe um Angulo?" )
                            Leia (Angulo)
                            S <- Sen(GraupRad(Angulo))
                            C <- Cos(GraupRad(Angulo))
                            T <- Tan(GraupRad(Angulo))
                            Escreval ("Seno de ", Angulo, " É igual a ", S, ".")
                            Escreval ("Cosseno de ", Angulo, " É igual a ", C, ".")
                            Escreval ("Tangente de ", Angulo, " É igual a ", T, ".")
                            Escreva ("Obrigado Por Utilizare Nosso Conversor.")
Fimalgoritmo