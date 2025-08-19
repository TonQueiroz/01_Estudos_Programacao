agora = new Date()
diadasemana = agora.getDay()// Conta de domingo a sábado com de 0 a 6

console.log(diadasemana)
if (diadasemana == 0) {
    console.log('Domingo')
} else if(diadasemana==1){console.log('Segunda do if')}

//ou posso usarr o SWITCH

switch(diadasemana){
    case 0:
        console.log('Domingo')
        break
    
    case 1: 
        console.log('Segunda do switch')
        break
    
    case 2:
        console.log('terça')
    
    default:
        console.log('Você está em um dia não registrrado')
}