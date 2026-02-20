//Filtrar carros da hyundai

const carros = [
    {carro:'gol', marca :'Volks'}, 
    {carro:'iX35', marca :'Hiunday'}, 
    {carro:'SantaFé', marca :'Hiunday'}, 
    {carro:'Polo', marca :'Volks'}
]

const carHiunday = carros.filter(filtrar)

function filtrar(valor,indice,array){

    return valor.marca =='Hiunday'
}

console.log(carHiunday)


//Arrow Function // 
const carHiundayArrow = carros.filter( valor => valor.marca =='Hiunday')

console.log(carHiundayArrow)