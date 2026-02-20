function processar(callbackSucesso, callbackErro){ //

    console.log('Processou')

    let resultadoProcessamento = true

    if  (resultadoProcessamento){ //Descobri que não preciso colocar o = a true no teste de variavel com if
        callbackSucesso()
    }else{
        callbackErro()
    }    
}

function salvarResultado(){ //Função com nome.
    console.log('Salvou Conteúdo com callbackSucesso')
}

const cancelarSalvamento = function (){ // função anonima guardada em variavel.
    console.log('Não salvou conteúdo com callback')
}


processar(salvarResultado,cancelarSalvamento)//passando as funções como parametro de outra função;