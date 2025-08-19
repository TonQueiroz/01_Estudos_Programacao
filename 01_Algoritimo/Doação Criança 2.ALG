Algoritmo "semnome"
// Disciplina   : [Criança esperança 2]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 18/02/2023
Var
// Seção de Declarações das variáveis
    D, Doa, Ov :Real
    Conf: Caractere

Inicio
  Escreval (" Bem vindo ao Criança esperança, Quanto gostaria de doar?")
  Escreval (" -------------------- ")
  Escreval (" Digite 1 para doar 10R$ ")
  Escreval (" -------------------- ")
  Escreval (" Digite 2 para doar 20R$ ")
  Escreval (" -------------------- ")
  Escreval (" Digite 3 para doar 30R$ ")
  Escreval (" -------------------- ")
  Escreval (" Digite 4 para doar outro valor")
  Escreval (" -------------------- ")
  Escreval (" Digite 5 para doar para cancelarR$ ")
  Leia (D)
  
  Escolha (D)

            Caso 1
                 Doa <- 10
          
            Caso 2
                 Doa <- 20
          
            Caso 3
                 Doa <- 10
            Caso 4
                 Escreval ("Quanto gostaria de doar?")
                 LEia (OV)
                 Doa <-  OV

          Caso 5 ou Outrocaso
                           Escreval ("Você cancelou sua doação.")


  FimEscolha
         Se (D=1)ou (D=2)ou (D=3)ou (D=4) Então
                Escreval ("Quer confiormar a doação de ", Doa, "R$? [S/N]")

                 Leia (Conf)
                 
                 Se (Conf = "S") ou (Conf = "s") Entao
                 
                    Escreval ("Sua doação de ", Doa, "R$, foi efetuada com sucesso?" )

                 Fimse
         Senao
         Escreval ("Sua doação não foi efetuada. O Criaça esperança agradece, Obrigado pelo seu contato.")
         Fimse



Fimalgoritmo