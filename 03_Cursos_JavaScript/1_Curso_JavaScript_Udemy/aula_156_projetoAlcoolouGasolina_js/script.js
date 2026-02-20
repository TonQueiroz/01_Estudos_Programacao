
function ValidarDados(d1,d2){

    if (d1 ==='' || d2 ===''){
        return false  
             
    } else { 
        return true
    }
}




function Calcular(){

var valorAlcool = document.querySelector('input#vAlcool').value //pegando o valor do Alcool

var valorGasolina = document.querySelector('input#vGasolina').value //pegando o valor da gasolina

let validar2 = ValidarDados(valorAlcool, valorGasolina)

if (validar2 === false){
    window.alert('[ERRO] INSIRA OS DADOS NOS CAMPOS!')

}else{

var nValAlcool = Number(valorAlcool)

var nValGasolina = Number(valorGasolina)

var porGasolina = (nValGasolina/100)*70

 
if (nValAlcool<porGasolina){
    var camporesultado = document.querySelector('p.pSaida')
    

    camporesultado.innerHTML = 'Melhor usar Alcool'
    
        
} else{
    var camporesultado = document.querySelector('p.pSaida')

    camporesultado.innerHTML = 'Melhor Gasolina' 
}
}
}

/*Criando novo Parágrrafo
var camporesultado = document.querySelector('p.pSaida')

var criarpar = document.createElement('p')

criarpar.value('Melhor usar Alcool')

criarpar.value('Melhor usar Gasolona')

*/

//window.alert(valorGasolina)