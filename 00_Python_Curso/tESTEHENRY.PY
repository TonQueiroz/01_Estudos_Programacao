# Usa as letras das palavras para criar os espaços vazios.
def blank():
    for _ in range(num_blank_word):
        blank_list.append("_ ")
    full_blank_word = "".join(blank_list)
    print(full_blank_word)

# Verificar se a letra que o usuário adivinhou (user_letter) está entre as letras da chosen_word.
def verify():
    global player_life
    for i in range(num_blank_word):
        if chosen_word[i] == guess:
            # Substituir o correspondente espaço vazio na lista blank_list pela letra correta.
            blank_list[i] = guess
            
    if guess not in chosen_word:
        player_life -= 1
        print(player_life)
    print(blank_list)


import random
player_life = 6
word_list = ["sociedade", "igual", "gás", "maquiagem", "polegada", "consistência"]
blank_list = []
# Escolha aleatória da palavra.
chosen_word = random.choice(word_list)
# Pega a quantidade de letras da palavra sorteada.
num_blank_word = len(chosen_word)

'''print(chosen_word)'''

# Escolha da letra pelo usuário. +
blank()
guess = input("\n Guess a letter: ").lower()
end_game = False

verify()

while not end_game:
    guess = input("\n Guess a letter: ").lower()
    verify()
    if '_ ' not in blank_list:
        end_game = True
        print("You Win.")
    if player_life == 0:
        print("ENFORCADO")
        break
    else:
        print(".")
