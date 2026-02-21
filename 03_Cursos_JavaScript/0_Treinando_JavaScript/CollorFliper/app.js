const colors = ['green', 'red','rg9ba(133,122,200)', "#f15025"];
const btn = document.getElementById('btn');
const color = document.querySelector('.color');

//evento ao clicar o botão
btn.addEventListener('click', function(){
    const randomNumber = getRandonNumber();       
    document.body.style.backgroundColor = colors[randomNumber]; 
    color.textContent = colors[randomNumber];
})

//função de número aletório no tamanho do array
function getRandonNumber(){
    return Math.floor(Math.random()*colors.length); //*colors.length multiplica o número aleatório pelo tamanho do array retoanando um numero aleatório entre 0 ee o tamanho do array //.Floor metodo para pegar apenas o número inteiro
}