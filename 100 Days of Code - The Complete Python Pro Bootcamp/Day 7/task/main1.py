import random
# NO COMMENTS VERSION

game_over = False

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

placeholder = ""
for char in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

stored_guess = ""

while game_over == False:

    guess = input("Guess a letter: ").lower()
    print(guess)

    stored_guess += guess

    for char in chosen_word:
        if char == guess:
            print("Right")
        else:
            print("Wrong")



    display = ""
    
    for char in range(len(chosen_word)):
        
        for letter in stored_guess:
            
            if chosen_word[char] == letter: 
                display += letter
                if placeholder[char] == "_":
                    placeholder= placeholder[:char] + letter + placeholder[char+1:]
                    if placeholder == chosen_word:
                        game_over = True
    print(placeholder)

print("You win")