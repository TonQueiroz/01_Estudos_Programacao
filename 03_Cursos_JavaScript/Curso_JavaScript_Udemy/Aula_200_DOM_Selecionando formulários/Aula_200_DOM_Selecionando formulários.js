const obj = document.getElementsByTagName('cadastro') //posso selecionar o formulario inteiro ou itens do formulário 
console.log (obj)


const todos = document.forms //pega todos os formulários como uma coleção

console.log (todos)



console.log(document.cadastro) //pega todos os formulários cadastro como uma coleção

console.log(document.cadastro.nome) //se tiver só um form com nome cadastro cadastro pega na posição com name nome


//configura ou define um valor inicial diretamente nesse value nome
document.cadastro.nome.value  = 'Ton'

//configura ou define um valor inicial diretamente nesse formulário name sexo para value masculino 
document.cadastro.sexo.value  = 'masculino'


//DESAFIO -- criar botão e com esse botão condigura um texto email nome e  sexo do formuulário.

