const fabricaFunção = function (nomex, preçox){ // é uma função que fabrica objetos de forma literal - é apenas.
    return{
        nome: nomex,
        preço: preçox,
        recuperarAvaliações(){
            console.log(`Avaliações de ${this.nome}`)
        }
    }
}

const carro1 = fabricaFunção('corsa', 10000)



const celular = fabricaFunção('iphone13', 3500)



celular.recuperarAvaliações()

console.log(carro1.nome,carro1.preço)