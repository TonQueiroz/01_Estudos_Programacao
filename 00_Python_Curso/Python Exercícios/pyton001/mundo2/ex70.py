#LOJA SUPER BARATÃO! LEIA NOME E PREÇOS DE VARIOS PRODUTOS! CONTINUA?  QUALO O TOTAL DE GASTOS NA COMPRA?  QUANTOS PRODUTOS CUSTAM MAIS DE 1000? QUAL O NOME DO PRODUTO MAIS BARATO?
sm = pcaro = cprod= pbar = 0

while True:

    p = str(input('Qual o nome do produto ?'))

    preço = float(input('Preço do produto?'))
    #contador de produtos   
    cprod += 1

    # Total da conta
    sm += preço

    # produtos 1000+

    if preço > 1000:
        pcaro += 1

    # Nome do produto mais barato

    if cprod == 1 or preço<pbar :
        pbar = preço
        npbar = p

    #condição de saída
    while saida not in 'SN' :
        saida = str(input('Você gostaria de cadastrar mais um produto?')).upper().strip()[0]
        if saida not in "SN": #Tratamento de excessões saída
            print('Digite uma entrada válida!')
      
    if saida== "N":
        break #Saída While Cadastro

print(f''' O Total gasto em {cprod} produdos foi R${sm:.2f}.
Produtos que foram mais de R$1000,00 foram {pcaro}.
O nome do produto mais barato é {npbar} e custou apenas R${pbar:.2f}.''')








