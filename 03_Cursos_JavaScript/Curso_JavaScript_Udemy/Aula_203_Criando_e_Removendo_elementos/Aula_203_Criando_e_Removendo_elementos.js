const ul = document.getElementById('listacompleta')
const li = document.createElement('li')
//const texto = document.createTextNode('Adicionado')

const ulfilha = document.createElement('ul')
const lifilha = document.createElement('li')






function adicionar(){
    
    //li.appendChild(texto)
    ul.appendChild(li)
    lifilha.textContent='teste'
    
    li.appendChild(ulfilha)
    ulfilha.appendChild(lifilha)

    ul.insertBefore(li, ul.children[1]) // Escolhe em qual posição vai inserir.
}

function remover(){
    
    li.removeChild(ulfilha) //retira o elemento
    
}

function Clonar(){

    const itemclone  = document.getElementById('itemclonar')
    const item = itemclone.cloneNode(true) // clona o que está dentro do elemeento <p> no html no caso 'Elemento parágrafo a ser clonado' se tivesse outro elemento dentro do elemento tbm pegaria os elementos filhos // Se colocar false não pega os elementos filhos

    ul.appendChild(item)

}
