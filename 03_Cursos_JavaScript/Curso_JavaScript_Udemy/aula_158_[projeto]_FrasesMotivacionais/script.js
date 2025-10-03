/*
function ValidarDados(d1,d2){

    if (d1 ==='' || d2 ===''){
        return false  
             
    } else { 
        return true
    }

    

}*/

var fra = ['frase1', 'frase2', 'frase3', 'frase4', 'frase5', 'frase6', 'frase7','frase8','frase9', 'frase10'  ]

function Gerarfrase(){
let lFrase= document.querySelector('div.dFrase')

let nfEscolhida = numeroAleatorio(0,(fra.length-1)) 

lFrase.innerHTML = (fra[nfEscolhida])


}

function numeroAleatorio (min,max){
    return Math.floor(Math.random()*(max-min+1))+min; //math.floor() apenas numeros inteiros
}

/*Criando novo Parágrrafo
var camporesultado = document.querySelector('p.pSaida')

var criarpar = document.createElement('p')

criarpar.value('Melhor usar Alcool')

criarpar.value('Melhor usar Gasolona')

*/

//window.alert(valorGasolina)