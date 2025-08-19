function pedirCopoAgua(){
    return 'Copo Pedido'
}

//let retorno = pedirCopoAgua()

//console.log(retorno)

//comprar arroz

function comprarArroz(dinheiro){

    console.log('Pegar Transporte')
    console.log('Entrar no mercado')
    console.log('Pegar Arroz')
    console.log('Pagar Arroz com dinheiro')
    let arroz = 15
    let troco = dinheiro -  arroz


    return 'Arroz comprado, o troco foi '+troco
}

console.log(comprarArroz(22))