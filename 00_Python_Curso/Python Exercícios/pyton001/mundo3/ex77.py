#Faça uma tupla com palavras aletórias
#Quais vogais estão nas palavras

tupla = ("Lua", "coragem", "sonho", "vento", "chave", "caminho", "fogo", "mar", "rocha", "vida", 'ouro')

for cont in tupla:
    palavra = cont.upper()
    #Minha Resoção
    ''' print(f'\n A palavra {palavra} tem as vogais ', end='')

    for c in range (0, len(palavra)) :
        if palavra[c] in 'AEIOU':
            print(palavra[c], end=" " )
        if c == (len(palavra)-1):
            print('\n')'''

#RESOLUÇÃO PROFESSOR
    print(f'\n A palavra {palavra} tem as vogais ', end='')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra, end=" " )

        
