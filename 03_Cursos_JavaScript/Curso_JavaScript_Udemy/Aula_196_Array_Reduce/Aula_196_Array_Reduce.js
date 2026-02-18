let user = [ 
    3,6,12,1 
]


userFiltrado= user.reduce(reduzir,10) //reduzir é a função e 10 é o valor inicial  - Soma/acumula todos os valores + o 10


function reduzir(acumulador,VALOR , INDICE, ARRAY){ //  VC CONSEGUE PEGAR ESSES 4 PARAMETROS primeiro o acululador(valor inícial) passado DO ARRAY VALOR INDICE E O ARRAY COMPLETO
    
        return acumulador+VALOR // acumula os valores começando em no valor inicial 10
    }
        

console.log(userFiltrado)

