let nome = prompt ('Qual seu nome?');
let idade = Number(prompt('Qual sua idade?'));
let linguagem = prompt('Qual linguagem de prohgramação está estudando');

alert(`Olá ${nome}, você tem ${idade} anos e já está aprendendo ${linguagem}!`)

let gosta = prompt('Você está gostando de aprender JavaScript ? S/N')

if (gosta=='S' || gosta=='s'){
    alert('Muito bom! Continue estudando e você terá muito sucesso.')
    
} else if (gosta=='N'  || gosta=='n'){
    alert('Ahh que pena... Já tentou aprender outras linguagens?')
} else {
    alert('informação inválida')
}