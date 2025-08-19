class Animal { //classe pai ou superclasse
    constructor(){
        this.cor = ''
        this.tamanho = 0
        this.peso = 10

    }
    correr(){
        console.log('correu(Classe pai)')
    }

    dormir(){
        console.log('dormiu')
    }
}



class Cao extends Animal {    // subclasse filho ou subclasse de animal herda propriedades e metodos de animal e podem ser usadas pelos objetos instanciados -- A palavra extends faz cão herdar de Animal
    constructor(){
        super() // Operador SUPER! USADO para criar atributos específicos em subclasses/classes filhas
        this.tamanhoOrelha = 'Tamanho Orelha '+ 30000 //atributo específica das classes filhas
    }

    latir(){ //Metodo apenas de Cão, n~pode ser usado por passaro
        console.log('Latiu') 
    }

    
}

class Passaro extends Animal {    // subclasse filho ou subclasse de animal herda propriedades e metodos de animal e podem ser usadas pelos objetos instanciados
    constructor(){
        super()
        this.corPenas = 'cinza'
    }

    voar(){ // Metodo apenas de passaro, n~pode ser usado por Cão.
        return 'vOOU'        
    }
}

class Papagaio extends Passaro{
    

    correr(){ // Incrementando o metodo da classe pai na classe filho usando o operador super.metopdo()
        super.correr()
        console.log('Correndo como um papagaio(Herdado da classe pai mas especificado na classe filho com o operador super')
    }
    falar(){
        console.log('Papagaio Falou')
    }
    
}

const passarinho1 = new Passaro

console.log (passarinho1.voar());





// usando o atributo específico de cão depois do operador  -- super()
const cachorrinho1 = new Cao
/*cachorrinho1.peso = 50
cachorrinho1.tamanho = 100
cachorrinho1.cor = 'Caramelo'*/

/*console.log(cachorrinho1.peso)
console.log(cachorrinho1.tamanho)
console.log(cachorrinho1.cor)*/
console.log(cachorrinho1.tamanhoOrelha) //atributo específico de caão gerado com um novo construtor e operador super
cachorrinho1.latir()
const cachorrinho2 = new Cao
console.log(cachorrinho2.tamanhoOrelha)

//Usando os atributos herdados de animal e de passaro na subclasse papagaio

const papagaio1 = new Papagaio;

papagaio1.correr() //metodo de animal // // Incrementado na classe filho usando o operador super.metopdo() Mudar ações/metodos subrescrevendo ou adicionando é chamado de POLIMORFISMO
papagaio1.voar() //metodo de passaro
console.log(papagaio1.corPenas) //atributo específico de passaro crido com um novo construtor  e operador super na classe passaro


papagaio1.falar() //metodo de papagaio



