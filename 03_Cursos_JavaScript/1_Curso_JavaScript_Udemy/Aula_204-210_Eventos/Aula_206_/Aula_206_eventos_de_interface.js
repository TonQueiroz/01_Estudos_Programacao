
const texto = document.querySelector('.texto')

window.addEventListener('load', function(){
    texto.textContent = "Evento Load"
    console.log('usou o evendo carregado Load');
        
})

function unloadfunction(){
    console.log('usou o evendo carregado Load');
}

window.addEventListener('unload', unloadfunction)

window.addEventListener('error', function(){
    //ver no console
    texto.textContent = "erro"
    console.log('usou o evendo carregado Load');
})

window.addEventListener('resize',function erro(){
    //ver no console
    texto.textContent = "usou o eveno resize"
    console.log('usou o eveno resize');
}) 

window.addEventListener('scroll', function(){
    texto.textContent = "usou o evento scroll "
})