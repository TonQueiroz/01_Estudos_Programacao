algoritmo "IMC"
// Disciplina   : [SE]
// Professor   : Curso em Vídeo
var
   A,  P, IMC : Real
   Tapa : Inteiro
inicio
   EscrevaL ("Qual sua altura (m))?")
   Leia (A)
   EscrevaL ("Qual o seu peso? (kg)")
   Leia (P)
   IMC <- (P / (A^2))
   EscrevaL (IMC)
            Se  (IMC < 17) entao
                EscrevaL ("Voce está MUUITO abaixo peso ideal")
                EscrevaL ("Coma mais dois X-Tudos!")
            Fimse

            Se  (IMC < 18.5) e (IMC >= 17) entao
                EscrevaL ("Voce está um pouco abaixo peso ideal")
                EscrevaL ("Deve comer mais um X-Tudo!")
            Fimse
            
            
        
            Se  (IMC >= 18.5) e (IMC < 25) entao
            EscrevaL ("Voce está um pouco abaixo peso ideal")
            EscrevaL ("Você está dentro do seu peso ideal! PARABENS!! \0/ Pode comer o que quiser, mas cuide-se para continuar saldavel")
        Fimse
        
        
          Se  (IMC >= 25) e  (IMC <= 30) então
              EscrevaL ("Quer o tapa na cara (Digite 1) ou o consolo (Digite 2) ?")
              LEia (Tapa)
              EscrevaL ("Voce esta em sobrepeso")
                        se (Tapa = 1) entao
                                EscrevaL ("Se está emagrecendo, parabéns!! está chegando no seu objetivo não para ein caralho!! se você está engordando toma vergonha na cara!")
                        senao
                               EscrevaL ("Se está emagrecendo, parabéns!! está chegando no seu objetivo, só Toma cuidado!! Você está um pouco acima do peso, Melhor se cuidar pra não perder a linha.")
                        Fimse
          Fimse

          Se  (IMC >= 30) e  (IMC <= 35) então
              EscrevaL ("Quer o tapa na cara (Digite 1) ou o consolo (Digite 2) ?")
              LEia (Tapa)
              EscrevaL ("Voce esta obeso!")
                        se (Tapa = 1) entao
                                EscrevaL ("Você ta fudido pacaraio, vai se cuidar porra!")
                        senao
                               EscrevaL ("Se está emagrecendo, parabéns!! está chegando no seu objetivo! ainda temos mas você consegue !! se está engordando ja deu merda isso aí ein!?")
                        Fimse
          Fimse
          
          Se  (IMC >= 35) e  (IMC <= 40) então
              EscrevaL ("Quer o tapa na cara (Digite 1) ou o consolo (Digite 2) ?")
              LEia (Tapa)
              EscrevaL ("Você está em obesidade severa!")
                        se (Tapa = 1) entao
                                EscrevaL ("Você ta na merda ein?! Vai morre porra!")
                        senao
                               EscrevaL ("Você precisa se cuidar, a situação está crítica.")
                        Fimse
          Fimse
          
          Se  (IMC >= 40) então
              EscrevaL ("Quer o tapa na cara (Digite 1) ou o tapa na cara? (Digite 1) ?")
              LEia (Tapa)
              EscrevaL ("Você está em Obesidade Morbida!")
                        se (Tapa = 1) entao
                                EscrevaL ("ME CONVIDA PRO VELÓRIO E DEIXA A CERVEJA PAGA.")
                        Fimse
          Fimse
fimalgoritmo