function fcontagem(){

var ent =  document.querySelector('input#entrada').value
var fim = document.querySelector('input#fim').value
var passo = document.getElementById('passo').value


if (ent===''||fim===''||passo===''){
    document.querySelector('p#txtresp').innerHTML='Impossível contar'
}else{
    ent = Number(ent)
    fim = Number(fim)
    passo = Number(passo)
    document.querySelector('p#txtresp').innerHTML='Contando'
    var resp = document.querySelector('p#contresp')
    
    resp.innerHTML=''

    if (passo==0) {   
        window.alert('Passo 0 Inválido Alterado para PASSO = 1')     
        passo=1
    }

    for (c = ent; c <= fim; c += passo) {

            resp.innerHTML+=` ${c} --> \u{1F449} `;
            
        }
        resp.innerHTML += ('\u{1F37B}')
    
    }


}



  
