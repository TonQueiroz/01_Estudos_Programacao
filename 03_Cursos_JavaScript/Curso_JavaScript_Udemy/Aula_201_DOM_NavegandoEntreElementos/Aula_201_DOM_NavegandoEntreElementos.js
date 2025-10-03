const lista = document.querySelector('div#itens')


console.log(lista)
//Abaixo seleciona elementos sem considerando os espaços como filhos tipo text
console.log(lista.parentNode) //Seleciona pai

console.log(lista.childNodes)

console.log(lista.f0irstChild)

console.log(lista.nextSibling) //seleciona irmão

console.log(lista.previousSibling)//seleciona irmão

//Abaixo seleciona elementos SEM considerar os espaços como filhos tipo text

console.log(lista.children)

console.log(lista.firstElementChild)

console.log(lista.lastElementChild)

console.log(lista.nextElementSibling)//seleciona irmão

console.log(lista.previousElementSibling)//seleciona irmão
