const hex = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F'];

const btn1 = document.getElementById('btn1');
const btn2 = document.getElementById('btn2');
const btn3 = document.getElementById('btn3');
const btnremov = document.getElementById('btnremov');
const color = document.querySelector('.color');

//função de número aletório no tamanho do array
function getRandonNumber(){    
   return Math.floor(Math.random()*hex.length); 
   //*colors.length multiplica o número aleatório pelo tamanho do array retoanando um numero aleatório entre 0 ee o tamanho do array //.Floor metodo para pegar apenas o número inteiro   
}

//-------------------------------------------------------------------------------------//

//Abordagem1 - evento pelo HTML
function trocarcor(){
    let numhex = "#"
    //concatenou 6 itens do arrar hex na variavel
    for (let index = 0; index < 6; index++){        
    numhex += hex[getRandonNumber()]       
    }
    console.log(numhex);
    //alterando background do html
    document.body.style.backgroundColor = numhex; 
    //alterando Texto do html  
    color.textContent = numhex +" - Evento através do HTML ou JS Abordagem 2";    
}

//-------------------------------------------------------------------------------------//

//Abordagem2 - evento pelo JS com variavelcomelementoDOM.propriedade
btn2.onclick = trocarcor2
function trocarcor2(){
    let numhex = "#"
    //concatenou 6 itens do arrar hex na variavel
    for (let index = 0; index < 6; index++){        
    numhex += hex[getRandonNumber()]       
    }
    console.log(numhex);
    //alterando background do html
    document.body.style.backgroundColor = numhex; 
    //alterando Texto do html  
    color.textContent = numhex +" - evento no JS Abordagem 2 - evento onclick como propriedade da variavel do btn2";    
}

//-------------------------------------------------------------------------------------//

//Abordagem3 -  Com Escutadores Listener com condição if para rodar em navegadores IE que não acxeitam addEventListener.
if (btn3.addEventListener){
    btn3.addEventListener('click', function(){
        let numhex = "#"
        //concatenou 6 itens do arrar hex na variavel
        for (let index = 0; index < 6; index++){        
        numhex += hex[getRandonNumber()]       
        }
        console.log(numhex);
        //alterando background do html
        document.body.style.backgroundColor = numhex; 
        //alterando Texto do html  
        color.textContent = numhex + " - Evento com addEventListener - Escutadores ";
})}else{
        btn3.attachEvent('click', function(){ //AtachEvent ´pe pra rodar no EInternetExplores antigo
        let numhex = "#"
        //concatenou 6 itens do arrar hex na variavel
        for (let index = 0; index < 6; index++){        
        numhex += hex[getRandonNumber()]       
        }
        console.log(numhex);
        //alterando background do html
        document.body.style.backgroundColor = numhex; 
        //alterando Texto do html  
        color.textContent = numhex + " - Evento com addEventListener - Escutadores ";})
}

//-------------------------------------------------------------------------------------//

//Removendo Evento Listener
btnremov.removeEventListener("click",function(){
    let numhex = "#"
    //concatenou 6 itens do arrar hex na variavel
    for (let index = 0; index < 6; index++){        
    numhex += hex[getRandonNumber()]       
    }
    console.log(numhex);
    //alterando background do html
    document.body.style.backgroundColor = numhex; 
    //alterando Texto do html  
    color.textContent = numhex + " - Evento com addEventListener - Escutadores ";
})


