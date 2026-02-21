const hex = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F'];

const btn = document.getElementById('btn');
const color = document.querySelector('.color');

btn.addEventListener('click', function(){
    let numhex = "#"
    //concatenou 6 itens do arrar hex na variavel
    for (let index = 0; index < 6; index++){        
    numhex += hex[getRandonNumber()]       
    }
    console.log(numhex);
    //alterando background do html
    document.body.style.backgroundColor = numhex; 
    //alterando Texto do html  
    color.textContent = numhex;
})
//função de número aletório no tamanho do array
function getRandonNumber(){    
   return Math.floor(Math.random()*hex.length); 
   //*colors.length multiplica o número aleatório pelo tamanho do array retoanando um numero aleatório entre 0 ee o tamanho do array //.Floor metodo para pegar apenas o número inteiro   
}