//Disponibilidade de Quartos

// Procedural - Baseado en Funcções e Variáveis

let quartos = 20
let Disponiveis = 10

function verrificarDisponibilidade (q,d){

    let vagas = q - d

    console.log(`Quartos disponíveis = ${vagas}`)
    
}

verrificarDisponibilidade(quartos,Disponiveis)

//Orientado a objetos - Baseado em Objetos cada variavel se torna um atributo(propriedade) cada função se torna um metodo;

const hotel = {
    quart: 20,
    ocupados : 10,
    verfDispo : function(){
        quartDisp =  (this.quart - this.ocupados )
        console.log(`Quartos dispníveis POO = ${quartDisp}`)
    }

}

hotel.ocupados = 2
hotel.verfDispo()

