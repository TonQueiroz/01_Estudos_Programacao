Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Curso em vídeo
// Descrição   : Determinar a quantidade de dependentes do funcionario (função)
// Autor(a)    : Ton Queiroz
// Data atual  : 21/02/2023
Var
 Fun, porc : Caractere
 Sal, aum, NSal : Real
 Dep : inteiro


Inicio
    Escreval("Qual o Nome do Funcionário?")
    Leia (Fun)
    Escreval("Qual o salário do funcionário?")
    leia (Sal)
    Escreval("Qual a quantidade de dependentes do funcionário?")
    leia (Dep)
    
    Escolha (dep)
            Caso (0)
            Aum <- (Sal*0.05)
            Porc <- ("5%")

            Caso 1,2,3
            Aum <- (Sal*0.1)
            Porc <- ("10%")
            
            Caso 4,5,6
            Aum <- (Sal*0.15)
            Porc <- ("15%")
            
            OutroCaso
            Aum <- (Sal*0.18)
            Porc <- ("18%")
            
    fimescolha
    
    NSal <- (Sal+Aum)
    
    Escreval ("O salário do funcionário será aumentado em ", porc, " que dará ", (aum), "R$ e será igual a ", (nsal), "R$.")

Fimalgoritmo