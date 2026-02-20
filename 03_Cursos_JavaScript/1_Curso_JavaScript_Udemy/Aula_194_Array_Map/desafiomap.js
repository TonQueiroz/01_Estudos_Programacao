// converter com map o dolar para real (CADA DOLAR = 3 REAIS)

const produtosDolar = [
    {produto:'notebook', preço:1200, moeda :'$'}, 
    { produto:'Celular', preço:800, moeda:'$'}
]
console.log(produtosDolar)

/*let produtosReal = produtosDolar.map(TranfReal)

function TranfReal(valor, indice, array){   
    let produtors = valor[1]
    let preçors = valor.preço*3
    let moedars = 'R$'

    return {produtors , preço:preçors, moeda: moedars}
}*/

//função acima comentada passada como Arrow Fuinction 

produtosReal = produtosDolar.map(valor=>{

    let produtors = valor[1]
    let preçors = valor.preço*3
    let moedars = 'R$'

    return {produtors , preço:preçors, moeda: moedars}
})

console.log('--PRODUTOS EM REAL--' )
console.log(produtosReal) 

console.log('--PRODUTOS EM Dolar--' )
console.log(produtosDolar)