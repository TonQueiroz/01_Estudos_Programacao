algoritmo "IMC"
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

           Se  (IMC < 18.5) entao
            EscrevaL ("Voce está um pouco abaixo peso ideal,")
            EscrevaL ("Mas Pelo menos você pode comer mais um X-Tudo! Mulher mais Gostooooosa do mundo!!! Te amo! <3")
        Fimse
          Se  (IMC > 25) então
              EscrevaL ("Quer o tapa na cara (Digite 1) ou o consolo (Digite 2) ?")
              LEia (Tapa)
              EscrevaL ("Voce está acima peso ideal")
                        se (Tapa = 1) entao
                                EscrevaL ("Se fudeu!! Toma vergonha na cara e vai cuidar da saúde ou vai perder sua namorada linda, maravilhosa e gostosa com força, que você ama muuuuito e depois vai ficar chorando igual um troxa!!")
                        senao
                                EscrevaL ("Vai lá! Confie no seu potencial! Ela não vai te deixar é verdade que ela gosta de você  gordinho!")
                        Fimse
          Fimse

          se  (IMC >= 18.5) e (IMC <=25) entao
              EscrevaL ("Você está dentro do seu peso ideal! PARABENS!! \0/")
          Fimse

fimalgoritmo