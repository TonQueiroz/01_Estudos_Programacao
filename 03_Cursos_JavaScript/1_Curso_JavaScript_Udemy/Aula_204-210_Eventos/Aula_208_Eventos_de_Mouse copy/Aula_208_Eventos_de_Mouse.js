
const digita = document.getElementById('entrada')
const texto = document.querySelector('.texto')

//QUANDO VOCÊ SEGURA A TECLA EXECUTA A FUNÇÃO VÁRIAS VEZES
digita.addEventListener('keydown', function(){
    texto.textContent = 'Tecla pressionada KeyDown sem caracteere ou enquanto segura uMa de caractere'
})

//Quando Você solta a tecla pressionada
digita.addEventListener('keyup', function(){
    texto.textContent = 'Tecla solta'
})

//só com teclas que tem caracteres QUANDO INSERE CARACTERES NÃO FUNCIONA PRA CSHIFT OU SETAS
//QUANDO VOCÊ SEGURA A TECLA EXECUTA A FUNÇÃO UMA VEZ
digita.addEventListener('keypress', function(){
    texto.textContent = 'Tecla pressionada de caractere'
})

