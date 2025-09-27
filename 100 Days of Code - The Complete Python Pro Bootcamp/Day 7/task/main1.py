import random


from hangmanwordsandart import word_list, HANGMANPICS, logo
# NO COMMENTS VERSION

state = 0
game_over = False

chosen_word = random.choice(word_list)

print(logo)
placeholder = ""
for char in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

stored_guess = ""

while game_over == False:
    print (HANGMANPICS[state])
    guess = input("Guess a letter: ").lower()
    print(guess)
    if guess.isalpha() == False or len(guess) != 1:
        print("You can only guess one letter at a time")
    if guess in stored_guess:
        print("You've already guessed that letter")
    if guess not in chosen_word:
        state += 1
        if state == 6:
            print (HANGMANPICS[state])
            game_over = True
            print(f"You lose. The word was {chosen_word}")
            break
    stored_guess += guess

    # for char in chosen_word:
    #     if char == guess:
    #         print("Right")
    #     else:
    #         print("Wrong")

    # display = ""
    
    for char in range(len(chosen_word)):
        
        for letter in stored_guess:
            
            if chosen_word[char] == letter: 
                # display += letter
                if placeholder[char] == "_":
                    placeholder= placeholder[:char] + letter + placeholder[char+1:]
                    if placeholder == chosen_word:
                        game_over = True
                        print("You win")
    print(placeholder)

