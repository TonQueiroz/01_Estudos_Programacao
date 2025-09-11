let frutas = [ 'Banana', 'Maça' , 'Peraa', 'Maracuja', 'pessego']

novoArray = frutas.map(reescrever)


function reescrever(VALOR , INDICE, ARRAY){ // COm O map VC CONSEGUE PEGAR ESSES 3 PARAMETROS DO ARRAY VALOR INDICE E O ARRAY COMPLETO
    return 'comi' + VALOR 
        
}
console.log(novoArray)

let arraydeobjetos = frutas.map(transfEmObj)

function transfEmObj(VALOR, INDICE, ARRAY){
    return {fruta: VALOR}

}

console.log(arraydeobjetos)