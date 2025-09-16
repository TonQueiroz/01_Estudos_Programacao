const nomes = [ 
    'Cleiton', 'Karen', 'Flora', 'Ravi'
]
//descobrir se e xiste algum produto em promoção(combinação de map com reduce)

let listaHTML = []

funcaoAcmuladora = function(acumulador, valorNome, i){
    return  acumulador += `<li>${valorNome}</li>`
}

listaHTML=nomes.reduce(funcaoAcmuladora,'')



console.log(listaHTML)







