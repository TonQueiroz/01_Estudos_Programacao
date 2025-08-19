class Carro{
    construtor(){
        this.modelo = 'gol'
        this.cor = "vermelho"
    }
    frear(){
        /*Não importa para o usuário se o freio é tambor ou disco ou se mudar de um pra outro, o carro simpleesmente freia */
                 console.log('Carro Freou')
    }
}

const carro1 = new Carro()

console.log(carro1.frear())