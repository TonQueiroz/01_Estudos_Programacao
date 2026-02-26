
const digita = document.getElementById('entrada')
const texto = document.querySelector('.texto')

//QUANDO VOCÊ CLICA NA CAIXA DE TEXTO
digita.addEventListener('focus', function(){
    texto.textContent = 'Caixa de texto Ganha foco - FOCUS'
    digita.style.backgroundColor = 'blue'
})

//Quando Você SAI DA CAIXA DE TEXTO
digita.addEventListener('blur', function(){
    texto.textContent = 'Caixa de texto perde o foco -  BLUR'
    digita.style.backgroundColor = 'brown'
})



