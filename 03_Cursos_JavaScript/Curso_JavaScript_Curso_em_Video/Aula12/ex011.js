var idade = 64
if (idade<16){
    console.log ('Não Vota')
    } else if(idade>=16 && idade<18 || idade>64){ //Não precisaria do idade>=16 pois já está em um bloco do primeiro if que só entra no else se for apenas maior que 16
            console.log('Voto Opcional')
        }else {//Aqui ele já pega os apenas maiores que 18
        console.log('Voto obrigatório')

    } 