const imagem = document.querySelector('#imagem')
//selecionando atributo
console.log(imagem.getAttribute('src')) 
console.log(imagem['src'])
console.log(imagem.src)

//alterando a atributo

function alterar (){
    imagem.src = 'img/507.png' //alterando a atributo
    
    const link = document.querySelector('#link')

    link.href ='https://www.youtube.com/'//alterando a atributo
    link.textContent = 'youtube'//alterando texto


}

