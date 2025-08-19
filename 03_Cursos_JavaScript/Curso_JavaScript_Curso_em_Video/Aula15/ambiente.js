let num = [12,6,32] // criando array

num.sort((a, b) => a - b) // Ordenando array  ordem crescente

num.sort((a, b) => b - a) // Ordenando array  ordem decrescente => significa um retorno



console.log(num.length) // criando array tamanho do array

console.log(num)

//num[1] = 7 //adicionando valor em posição específica

console.log(num)

num.push(35)  //adicionando valor  no final

console.log(num)

let cp = ['laranja', 'maçã', 'banana']

cp.sort()

console.log(cp)

//visitabo todos osvalores do vetor

for ( pos=0; pos<num.length; pos++){
    console.log(`A posição ${pos} tem o valor ${num[pos]}`)

}

for(var pos in cp){
    console.log(`A posição ${pos} tem o valor ${cp[pos]}`)
}

console.log(num.indexOf(6)) //IndexOf Retorna o a posição do indice do valror procurado
//se não tiver o valor ele retorna -1




