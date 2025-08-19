//Declarando/Criando Objetos

//------------------------------

//Notação literal

const hotel = {
    quart: 20,
    ocupados : 10,
    piscinas : 2,
    verfDispo : function(){
        quartDisp =  (this.quart - this.ocupados )
        console.log(`Quartos dispníveis POO = ${quartDisp}`)
    }

}


console.log(hotel.piscinas)

delete hotel.piscinas

console.log(hotel.piscinas)

//------------------------------

//notação de construtor (objeto em branco)

const hotel2 = new Object() //cria o objeto em brando

hotel2.quartos = 20         // adiciona atributos ou metodos
hotel2.ocupados = 10
hotel2.piscina = 2
hotel2.verfDispon = function(){
    quartDisp =  (this.quart - this.ocupados )
    console.log(`Quartos dispníveis POO = ${quartDisp}`)
}

//------------------------------
//Criando Classes ( mais simples)

class hotelclass {
    constructor(){
        this.quartos = 20         // adiciona atributos ou metodos ao objeto criado através do construtor da classe
        this.ocupados = 10
        this.piscina = 2
        
        }
        
    verfDispon = function(){
        let quartDisp = (this.quartos - this.ocupados )
        console.log(`Quartos dispníveis com construtor = ${quartDisp}`)
            
    }

    
}

const hotelNovo1 = new hotelclass()

const hotelNovo2 = new hotelclass()

const hotelNovo3 = new hotelclass()

hotelNovo1.verfDispon()


