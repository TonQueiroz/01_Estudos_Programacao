const colors = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F'];

const btn = document.getElementById('btn');
const color = document.querySelector('.color');

btn.addEventListener('click', function(){

    arraynumhex = []
    
    //Preenchendo arraynumhex com 6 valores, com índices aleatórios do array colors
    for (let index = 0; index < 6; index++) {        
        arraynumhex.push(colors[getRandonNumber()])       
    }

    //Criando Numero Hexadecimal com # e transformando Array em Texto
    numhex = '#'+ arraynumhex.join('');  

    //alterando background do html
    document.body.style.backgroundColor = numhex; 
    //alterando Texto do html  
    color.textContent = numhex;
})

function getRandonNumber(){    
   return Math.floor(Math.random()*colors.length); 
   //*colors.length multiplica o número aleatório pelo tamanho do array retoanando um numero aleatório entre 0 ee o tamanho do array //.Floor metodo para pegar apenas o número inteiro
   
}
