
var vnum = []


function adicionar(){
   
   var resp = document.querySelector('p#resposta')
   resp.innerHTML = ''

   var num = document.querySelector('input#num').value
   document.querySelector('input#num').value = '' // apagar a caixa de input
  

   if (num === ""){
   window.alert('[ERRO] IMPOSSÍVEL CONTINUAR. PORFAVOR INSIRA UM NÚMERO!')

   } else if (num<1 || num>100){
      window.alert('[ERRO] NUMERO INVÁLIDO. PORFAVOR INSIRA UM NÚMERO ENTRE 0 E 100!')

   } else if(vnum.indexOf(Number(num))!==-1){ //SIGHNIFICA QUE ELE TA NA LISTA -- posso trocar por vnum.includes(num)
      
      window.alert('[ERRO] NUMERO JÁ INSERIDO. POR FAVOR TROQUE POR UM NOVO!')
   
   }else{
    num = Number(num)
    
    
    vnum.push(num)
    
        
    adcslct(num)

    
   }
}

function adcslct(n){
   var slclist = document.querySelector('select#SelListNum')
   var nopção = document.createElement('option')
   nopção.innerHTML = `Valor ${n} adicionado!`

   slclist.appendChild(nopção)

}


function finalizar(){
if (vnum.length === 0){

   window.alert('[ERRO] LISTA VAZIA. PORFAVOR INSITA UM NÚMERO!')

}else{
   var soman = (somatotal(vnum))

   var maiorn = (maiornumero(vnum))

   var menorn = (menornumero(vnum))
   
   
   resp = document.querySelector('p#resposta')
   resp.innerHTML = `
   Temos ao todo ${vnum.length}. <br><br>

   A soma dos valores é ${soman}. <br><br>

   O maior valor informado foi ${maiorn}. <br><br>

   O menor valor informado foi ${menorn}. <br><br>

   A média dos valores doi  ${soman/vnum.length}. `
}
}


function somatotal(a){
   soma = 0
   for (pos in a)
      soma = soma+a[pos]

   return soma
}

function maiornumero(b){
   maior = 0
   for (i=0;i < b.length; i++){
      if (b[i]>maior) {
         maior = b[i]
      }
   }
   return maior

}

function menornumero(c){
   menor =101

   for(i in c){
      if (c[i] < menor){
         menor = c[i]
      }

   }
   return menor

}