function carregar(){
        var txthorario = document.querySelector('section#txtmutavel')

        txthorario.innerHTML = 'Texto mutável selecionado'

        var imghorario = document.querySelector('img#imgred')

        //imghorario.innerHTML = "IMAGEN SELECIONADA"

        var hour = new Date().getHours()
        var hour = 8
        
        if (hour < 5 && hour >=0){
            txthorario.innerHTML = `Agora são ${hour}hrs.<br> Boa Madrugada`
            imghorario.src = 'imagens/noite-redonda.png'
            document.body.style.background = '#363636'

        } else if( hour<12){ 
            txthorario.innerHTML =`Agora são ${hour}hrs.<br> Bom Dia`
            imghorario.src = 'imagens/manha-redonda.png'
            document.body.style.background = '#FFFAF0'
            document.querySelector('header').style.color = '#363636'
            document.querySelector('footer').style.color = '#363636'

        } else if (hour<18){
            txthorario.innerHTML = `Agora são ${hour}hrs.<br> Boa Tarde`
            imghorario.src = 'imagens/tarde-redonda.png'
            document.body.style.background = '#F4A460'
            
        } else if(hour<=24){
            txthorario.innerHTML =`Agora são ${hour}hrs. <br> Boa noite`
           imghorario.src = 'imagens/noite-redonda.png'
           document.body.style.background =' #1C1C1C'

        } else {
                window.alert('[ ERRO ] Horário Inválido')
            }
        
}