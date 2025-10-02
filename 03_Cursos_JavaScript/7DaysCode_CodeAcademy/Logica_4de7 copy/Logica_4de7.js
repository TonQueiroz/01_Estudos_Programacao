//começar
let numPC = ''
let meuNum = ''
let contador = 0
function sortear(){
    numPC = ((Math.random()*10)).toFixed(0)
    window.alert(numPC)
}

// Eu escolho o número
let pResultado = document.querySelector('#pResultado')

function pegarNum(){
    meuNum = document.querySelector('#NúmeroPC').value
        
    testarNum(meuNum, numPC)
    
}


function testarNum(NumTestado1, NumTestado2){
    
    //Testo o número com o computador

    //enqualto numero for diferente de  numero testado 2 e contador diferente de 2 faça
    

    if (NumTestado1==NumTestado2){
        pResultado.innerHTML = 'Parabéns Você acertou'
    } else { 
        pResultado.innerHTML = 'tente outra vez :('
        contador = contador+1 

        if (contador>=3){
            pResultado.innerHTML = 'Acabaram suas tentativas :('
        }
    }



}







//Se estiver certo parabéns se não tiver mais 2 tentativas

//Consegui parabéns!

//Não consegui? Quer tentar novamente com outro número ??

//Agradecimemnto



/*let area = Number(prompt ('qual área quer serguir? [1]FrontEnd ou [2]BackEnd'))
let tragetoria = ''

if (area == 1){
        tragetoria = 'FrontEnd'
}else if(area==2){
        tragetoria = 'BackEnd'
}

let listaTecnologias = []

if (area == 1) {
    let qualTec = prompt('Gostatia de aprender qual técnologia? [1]React ou [2]Vue?')
    if (qualTec == 1) {
        listaTecnologias.push('React')
    } else if (qualTec == 2){
        listaTecnologias.push('Vue')
    }

    alert( listaTecnologias )
    
} else if (area == 2) {
    let qualTec = prompt('Gostatia de aprender qual técnologia BACKEND? [1]C# ou [2]JAVA?')
    if (qualTec == 1) {
        listaTecnologias.push('C#')
    } else if (qualTec == 2){
        listaTecnologias.push('JAVA')
    }
}

let seguir = Number(prompt('O que você quer fazer após Seguir na seguir area escolhida ou se tornar um fullstack ?[1]SeguirÁrea [2]FullStack?'))

if (seguir == 2) {
    tragetoria = 'FullStack'
}    

let continuar = Number(prompt('Gostaria de aprender mais alguma técnologia?[1]Sim / [2]Não'))

while (continuar==1){
if (continuar==1){
    listaTecnologias.push(prompt('Qual Tecnologia gostaria de arender?')) //Adicionando técnologias a lista
    continuar = Number(prompt('Gostaria de aprender outra técnologia?[1]Sim / [2]Não'))//Decisão se continua no While    
}}

alert('Sua tragetória será ' + tragetoria + '! E as técnologias que você aprenderá são - '+ listaTecnologias+ '- Boa Sorte na siua tragetória')
*/