class Animal { //classe pai ou superclasse
    constructor(){
        this.cor = ''
        this.tamanho = 0
        this.peso = 10

    }
    correr(){
        console.log('correu')
    }

    dormir(){
        console.log('dormiu')
    }
}



class Cao extends Animal {    // subclasse filho ou subclasse de animal herda propriedades e metodos de animal e podem ser usadas pelos objetos instanciados -- A palavra extends faz cão herdar de Animal

    latir(){ //Metodo apenas de Cão, n~pode ser usado por passaro
        console.log('Latiu') 
    }

    
}

class Passaro extends Animal {    // subclasse filho ou subclasse de animal herda propriedades e metodos de animal e podem ser usadas pelos objetos instanciados
        voar(){ // Metodo apenas de passaro, n~pode ser usado por Cão.
             return 'vOOU'        
    }
}

const passarinho1 = new Passaro

console.log (passarinho1.voar());

const passarinho2 = new Passaro

console.log(passarinho2.peso)

const cachorrinho1 = new Cao
cachorrinho1.peso = 50
cachorrinho1.tamanho = 100
cachorrinho1.cor = 'Caramelo'

console.log(cachorrinho1.peso)
console.log(cachorrinho1.tamanho)
console.log(cachorrinho1.cor)

cachorrinho1.latir()

console.log(passarinho2.voar())