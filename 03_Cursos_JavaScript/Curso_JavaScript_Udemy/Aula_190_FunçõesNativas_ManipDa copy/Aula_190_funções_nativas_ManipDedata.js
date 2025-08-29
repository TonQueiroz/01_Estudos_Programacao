let data = new Date()
//baseado na data e hora do seru computador
data.toString()

console.log(data.toString())

console.log(data.getDate())

console.log(data.getMonth())

console.log(data.getHours())

console.log(data.getMinutes())

console.log(data.getSeconds())

//operações com datas hora minuros ou segundos


console.log(data.setDate(data.getDate() + 10) + 'Retorrnou o numero em Timestamp');

console.log(data.toString(), 'Adicionou 10 dias ao dia');

console.log(data.getDate())

data.setDate(data.getDate() + 10)

console.log(data.toString(), 'Adicionou 10 alem dos 10 adicionados antes');

console.log(data.getDate())
