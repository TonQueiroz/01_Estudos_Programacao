const colors = ['green', 'red','rg9ba(133,122,200)', "#f15025"];

const btn = document.getElementById('btn');
const color = document.querySelector('.color');

btn.addEventListener('click', function(){
    //console.log(document.body)
    //get randon number between 0 - 3 
    const randomNumber = getRandonNumber();
    console.log(randomNumber);    
    document.body.style.backgroundColor = colors[randomNumber];
    color.textContent = colors[randomNumber];
})

function getRandonNumber(){
    return Math.floor(Math.random()*colors.length ); //*colors.length multiplica o número aleatório pelo tamanho do array retoanando um numero aleatório entre 0 ee o tamanho do array //.Floor metodo para pegar apenas o número inteiro
}