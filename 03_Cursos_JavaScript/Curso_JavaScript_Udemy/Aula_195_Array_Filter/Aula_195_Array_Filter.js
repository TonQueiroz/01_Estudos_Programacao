let user = [ 
    {nome:'Ana' , idade:16},
    {nome:'Jailton', idade:53},
    {nome:' Kellen', idade:48}    
]


userFiltrado= user.filter(filtrar)


function filtrar(VALOR , INDICE, ARRAY){ //  VC CONSEGUE PEGAR ESSES 3 PARAMETROS DO ARRAY VALOR INDICE E O ARRAY COMPLETO
    
        return VALOR.idade<=18
    }
        

console.log(userFiltrado)

