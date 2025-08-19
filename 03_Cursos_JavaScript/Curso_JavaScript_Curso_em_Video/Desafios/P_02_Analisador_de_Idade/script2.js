 function btnverificar(){
            var txts = document.querySelector('p#txtmuts')//selecionei o parágrafo do texto femimnino ou masculino
            //txts.innerHTML = 'A imagem mudou ao clique'  // teste de seleção 
            var txt = document.querySelector('p#txtmut') //selecionei o parágrafo do texto do sexo 
            //txt.innerHTML = 'A imagem mudou ao clique'   // teste de seleção 
                       

            var img = document.querySelector('img#imgmut') //selecionei o parágrafo da imagem
            //img.innerHTML = 'A imagem mudou ao clique' // teste de seleção

            var anoatual = new Date().getFullYear() //peguei o ano de 2025

            var anodenascimento = Number(document.querySelector('input#anonasc').value) //peguei o ano de nascimento 
            var imgp = document.querySelector('p#recimag')
            // outro jeito é criar a imagem atraves do JS com var img = document.creatElemente('img').setAttribute('id','foto') com set atrubute vc atribuiu um id com o nome foto
            imgp.style.display = 'block'
           

            idade = anoatual - anodenascimento //cálculo de ano de mascimento            

            if (idade >0){
                if (document.querySelector('input[id="SexM"]:checked')){
                var Sexo = 'M'
                } else if (document.querySelector('input[id="SexF"]:checked')){
                Sexo = 'F'  
                } else{window.alert ('Selecione o Sexo')}

                
                switch (Sexo){

                    case "M":
                        txts.innerHTML = `Você é do sexo masculino` 
                        if (idade<10){
                            txt.innerHTML = `Você é um Menino de ${idade} anos `
                            img.src = 'Imagens/Criança-Redonda.png'
                        } else if (idade< 18) {
                            txt.innerHTML = `Você é um Adolescente de ${idade} anos `
                            img.src = 'Imagens/adolecente-redonda.png'
                            
                        } else if(idade<60){
                            txt.innerHTML = `Você é um Adulto de ${idade} anos `
                            img.src = "Imagens/adulto-redondo.png"

                        } else if (idade>60){
                            txt.innerHTML = `Você é um senhor de ${idade} anos `
                            img.src = "Imagens/velho-redonda.png"
                        }
                        

                        
                        break
                    case "F":
                        txts.innerHTML = "Você é do sexo feminino"

                        if (idade<10){
                            txt.innerHTML = `Você é um Menina de ${idade} anos `
                            img.src = 'Imagens/criança-redondaf.png'

                        } else if (idade< 18) {
                            txt.innerHTML = `Você é uma Adolescente de ${idade} anos `
                            img.src = 'Imagens/adolecente-redonda.png'
                            
                        } else if(idade<60){
                            txt.innerHTML = `Você é uma Adulta de ${idade} anos `
                            img.src = "Imagens/adulta-redondo.png"

                        } else if (idade>60){
                            txt.innerHTML = `Você é uma senhora de ${idade} anos `
                            img.src = "Imagens/velha-redonda.png"
                        }
                        

                        
                        break
                    default:
                        txts.innerHTML = '[ERRO] Sexo inválido'
                        break
                }
            } else{
                window.alert('[ERRO!] ANO DE NASCIMENTO INVÁLIDO')
            }               
            

        }
   