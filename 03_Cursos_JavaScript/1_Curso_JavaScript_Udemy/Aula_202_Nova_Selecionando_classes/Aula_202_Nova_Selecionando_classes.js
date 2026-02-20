
const obj = document.querySelector("span")
const classe = obj.classList

console.log(classe.length)

function executar(){
    const obj = document.querySelector("span")
    const classe = obj.classList
    classe.add('classe01', 'texto', 'buda') //adiciona a classe01 se já existe no css.
    //obj.className = 'classe02', 'texto', 'buda' // Altera Classe
    //classe.toggle('classe01') // Alterna entre classes Classe

    classe.forEach(item=>console.log(item))

    //console.log(classe) //Retorna a ou as classe da tag
    //console.log(classe.contains('classe0'')) verifica se existe a classe e retorna True ou false.
    
}

function Tirar(){
    const obj = document.querySelector("span")
    const classe = obj.classList
    classe.remove(classe[0]) //Remove
}