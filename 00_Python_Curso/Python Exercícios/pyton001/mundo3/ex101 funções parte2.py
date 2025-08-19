# Função chamda voto()  vai receber o ano de nascimento da pessoa 
# retornando um valor literal (Texto) indicando se a pessoa tem voto Negado, opcional ou obrigatório


def voto(id):
    from datetime import datetime

    idvoto = datetime.now().year - id
    if idvoto <16:
        return f'Você tem {idvoto} anos de idade e seu voto é NEGADO'
    elif idvoto >=16 and idvoto <18 or idvoto>64:
        return f'Você tem {idvoto} anos de idade e seu voto é opcional'
    elif idvoto >= 18 and idvoto < 65:
        return f'Você tem {idvoto} anus de idade O seu voto é Obrigatório'

idade = int(input('em que ano você nasceu?'))

resp = voto(idade)
print("~"*(len(resp)+4))
print(f'{'OBRIGATORIEDADE DE VOTO'}')
print("~"*(len(resp)+4))
print(f'  {resp:^}  ')
print("~"*(len(resp)+4))


    
    



