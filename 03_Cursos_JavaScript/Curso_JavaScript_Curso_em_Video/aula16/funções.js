// SE VOCÊ CLICAR E ARRASTAR PARA SELECIONAR O CÓDIGO E MANDAR EXECUTAR 
// ELE VAI EXECUTAR SÓ O CÓDIGO SELECIONADO PARA ESTUDO
function parimp(x){ // parimp nome da função -- x parametro formal
    if(x%2==0){
        var z = `O NÚMER ${x} É PAR`        
    } else{
        var z = `O NÚMERO ${x} É imPAR`
    }
    return z  // retorno da função
}

var respostaretorno = parimp(8) // parimp(8) é a chamada da função ---
//respostaretorno é a variável que recebe o retorno da cunção

console.log(respostaretorno)


//-----------------

function soma(n1,n2){
    return n1+n2
}

console.log(soma(2,5)) 

//-------------------------------

//colocando a função na variável a variável vira a chamada da função

var v = function(x){
    return x*2
}

console.log('funçao na variavel retornada direto no console log ' + v(3)) // e eu posso usar um console log 

ret= v(10) // ou colocar ela dentro de uma variável como uma funçao qualquer

console.log('O retorno da função v na variávrl ret é '+ ret)

//recursividade == quando uma função chama ela própria
//recursividade na dunção de fatorial (fatorial de 5!= 5*4*3*2*1  ou 5*4!)

function fatorial(x){
    if (x==1){
        return 1
    }else{
        return x * fatorial(x-1)
    }
}

resp = fatorial(57)
console.log(resp)

