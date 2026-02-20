const produtos = [ 
    {nome: 'Notebook',  promocao: true},
    {nome: 'Celular',  promocao: false}
]
//descobrir se e xiste algum produto em promoção(combinação de map com reduce)


const produtosPromo = produtos.map( 
    produto => produto.promocao // ARROw FUNCTION!! produto pega o valor do array produtos eue é o objeto  e produto.promoção pega o valor da chave promoção no objeto
)

//console.log(produtosPromo)

const funcao = function(acumulador, atual){
    return acumulador || atual // Aqui como acumulador e atual é true OU false se um dos dois forem true vai retornar true
}

const novo = produtosPromo.reduce(funcao)

console.log(novo)

if(novo){// aqui é o mesmo coceito não precisamos colocar  if(novo=True) que também estaria certo
    console.log('Tem Promoção')
} else {
    console.log('Não Tem Promoção')
}






