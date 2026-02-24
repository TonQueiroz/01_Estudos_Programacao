
const btn1 = document.getElementById('btn1')
const btn2 = document.getElementById('btn2')
const paragrafo = document.getElementById('paragmove')
const paragrafo2 = document.getElementById('paragmove2')

const texto = document.querySelector('.texto')

//QUANDO clica
btn1.addEventListener('click', function(){
    texto.textContent = 'Evento de CLICK'
})

//Quando Você CLICA 2 VEZES
btn1.addEventListener('dblclick', function(){
    texto.textContent = 'Evento de Double Click'
})

btn2.addEventListener('mousedown', function(){
    texto.textContent = 'Evento de mouse press'
})

btn2.addEventListener('mouseup', function(){
    texto.textContent = 'Evento de mouse up'
})

paragrafo.addEventListener('mouseover', function(){
    texto.textContent = 'Evento de Mouse Oveer'
})

paragrafo.addEventListener('mouseout',function(){
    texto.textContent = 'Evento de Mouse out'
})

paragrafo2.addEventListener('mousemove',function(){
    texto.textContent = 'Evento de MouseMove'
})

paragrafo2.addEventListener('mouseout',function(){
    texto.textContent = 'Evento de Mouse out'
})

//só com teclas que tem caracteres QUANDO INSERE CARACTERES NÃO FUNCIONA PRA CSHIFT OU SETAS
//QUANDO VOCÊ SEGURA A TECLA EXECUTA A FUNÇÃO UMA VEZ
digita.addEventListener('keypress', function(){
    texto.textContent = 'Tecla pressionada de caractere'
})

