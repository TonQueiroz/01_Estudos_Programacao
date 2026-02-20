//Eencapsulamento - modificadores dee acesso, Getters ee Setters

//GETTERS E SETTER São metodos especiais utilizados para esse contexto que são invovcados como atributos da classe e não como metodos por serem pseudoatributos;

class ContaBancaria{
    constructor(){
        this._numeroRealdaConta = 0 //_Significa que o atrinuto não deeve ser acessado dretameente só atravez dee getters ee setters
        this.saldo = 0 
    }

    get numeroConta(){// o get torna o meetodo numeroConta em um pseudo atributo
        return this._numeroRealdaConta //Aqui você acessa o numeero conta atravez do --get-- tendo acessando assum uma pseudoPropriedade ele te retorna o valor da propriedade, mas você não sabe realmente qual é ela por que vc acessa ela pelo --numeroConta-- e não por ela mesma --_numeroRealDaConta
    } 

    set numeroConta(numero){ //O set faz do numeroConta um Pseudo Atributo que pode ser altera com o sinal de atribuição que pode ser usado com testes de verificação para atribuir um valor válido ao atributo real
        if (numero > 0){
        this._numeroRealdaConta = numero //aqui você alterou o número real da conta
    }
    }
}



const conta1 = new ContaBancaria()
console.log(`Número conta bancária Real $'{conta1.numeroConta'} vinda do construtor`) //numero conta é um pseudo atributo, o atributo real ée _numeroRealdaConta que não é acessado diretamente para segurança(pq se alterar pode dar merda)

conta1.numeroConta = 30 // quando você usa o sinal de atribuição no pseudoAtributo/proprieedade --numeroConta-- Você eesta acessando o --set numeroConta(numero) e executando aqueele metodo com o bloco de código passando copmo mparametro 30 no lugar de  (numero) e no caso do bloco alterando o número da conta sem acessar diretamente _numeroRealdaConta

console.log( `O numero da conta foi alterado usando o  set para ${conta1.numeroConta} com set`)

const conta2 = new ContaBancaria()
console.log(conta2.numeroConta)


