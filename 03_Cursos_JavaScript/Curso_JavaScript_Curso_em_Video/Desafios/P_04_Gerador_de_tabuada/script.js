

 function gerar(){  
    
    

    var  numero = document.querySelector('input#num').value
    var respsel = document.querySelector('select#resposta')

    respsel.innerHTML = ''

    if (numero === ""){
        window.alert('[Erro] Campo vazio, digite um numero')
    }else{
        numero = Number(numero)

        c=0
        for (0; c<=10; c++ ){
            resposta = `${numero} x ${c} = ${numero*c}<br>`

            var novaopção = document.createElement('option')

            novaopção.value = c

            novaopção.innerHTML = resposta// ao invez do inner html ele usou o novaopção.text para adicionar a resposta

            respsel.appendChild(novaopção)

            
        }

    } 
            
    }