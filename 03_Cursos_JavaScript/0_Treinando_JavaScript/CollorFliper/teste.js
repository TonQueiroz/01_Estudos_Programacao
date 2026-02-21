const colors = [0,1,2,3,4,5,6,7,8,9, 'A', 'B', 'C', 'D','E','F'];

const numberhex = getRandonNumber();

console.log(numberhex);


function getRandonNumber(){
    let arrayehex =[]
    for (let i=0; i<6; i++){    
    indramd = Math.floor(Math.random()*colors.length)
    arrayehex.push(colors[indramd])
    }
    return  arrayehex.join('')
}

