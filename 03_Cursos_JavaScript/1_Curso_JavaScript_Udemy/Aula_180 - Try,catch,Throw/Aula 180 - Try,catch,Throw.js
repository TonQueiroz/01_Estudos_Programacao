function contarletras(x){
    try{
    console.log(x.nome.length)
    } catch( erro ){
        console.log('Deu erro aqui');
        tratarErro( erro )        
    }finally{
        console.log('Volte Sempre')
    }
}

const produto={
    nome:'Cleiton',
    idade:33
}

contarletras(produto)

function tratarErro( erro ){

    throw new Error("195");  

}