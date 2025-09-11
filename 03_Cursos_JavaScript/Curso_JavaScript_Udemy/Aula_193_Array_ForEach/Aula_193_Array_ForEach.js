let frutas = [ 'Banana', 'Maça' , 'Peraa', 'Maracuja', 'pessego']


frutas.forEach(escrever)


function escrever(VALOR , INDICE, ARRAY){ // CONO FOREACH VC CONSEGUE PEGAR ESSES 3 PARAMETROS DO ARRAY VALOR INDICE E O ARRAY COMPLETO

    
    if (VALOR == 'Peraa')
        VALOR = 'TROCOU PERA'

    console.log(VALOR + '-  POSIÇÃO =' +  INDICE + ' - Escrito com ForEach')

    console.log(ARRAY)
    
}