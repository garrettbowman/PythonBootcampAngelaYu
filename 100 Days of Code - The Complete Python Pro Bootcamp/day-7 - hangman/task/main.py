import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

chosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()
print(guess)

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
for char in chosen_word:
    if char == guess:
        print("Right")
    else:
        print("Wrong")


# STEP 2 
### TODO-1
# - Create an empty String called `placeholder`.
# - For each letter in the chosen_word, add a `_` to `placeholder`.
# - So if the `chosen_word` was "apple", `placeholder` should be `_ _ _ _ _` with 5 `"_"` representing each letter to guess.
# - Print out `hint`.

# <div class="hint">
#   Remember you can use the range() function inside a loop to carry out an action for a particular number of times. 
# </div>

placeholder = ""
for char in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

# ### TODO-2
# - Create an empty string called "display".
# - Loop through each letter in the `chosen_word`
# - If the letter at that position matches `guess` then reveal that letter in the `display` at that position.
# - e.g. If the user guessed "p" and the chosen word was "apple", then `display` should be `_ p p _ _`.
# - Print `display` and you should see the guessed letter in the correct position.
# - But every letter that is not a match is represented with a "_".

# <div class="hint">
#   Remember that the for loop will go through each letter in the chosen_word in order. You can use that fact to create a new string, appending the letter or an "_".
# </div>        

display = ""
for char in range(len(chosen_word)):
    if chosen_word[char] == guess:
        display += guess
    else:
        display += "_"
print(display)

# Step 3
# ### TODO-1
# - Use a while loop to let the user guess again. 
# - The loop should only stop once the user has guessed all the letters in the chosen_word.
# - At that point `display` has no more blanks ("_"). Then you can tell the user they've won.

# <div class="hint">
#   You can use the in keyword to check if a String or List contains a particular item. 

# e.g. Google: check if a letter is present in a string python 
# </div>




# ### TODO-2
# - Update the for loop so that previous guesses are added to the `display` String.
# - At the moment, when the user makes a new guess, the previous guess gets replaced by a "_". We need to fix that by updating the for loop.

# <div class="hint">
#   Think about how you can store the matched letters and use an elif to check if a letter has been matched before.
# </div>





# Step 4
# ### TODO-1: 
# - Create a variable called `lives` to keep track of the number of lives left.
# - Set `lives` to equal `6`.


# ### TODO-2: 
# - If `guess` is not a letter in the `chosen_word`, Then reduce `lives` by `1`. 
# - If `lives` goes down to `0` then the game should end, and it should print "You lose."

# <div class="hint">
#   The not in keywords will be your friend in this todo. You can check if something exists in the chosen_word completely separately from the rest of the code.
# </div>


# ### TODO-3: 
# - print the ASCII art from the list `stages` that corresponds to the current number of `lives` the user has remaining.


# Step 5
# ### TODO-1: 
# - Update the word list to use the `word_list` from hangman_words.py

# ### TODO-2: 
# - Update the code to use the `stages` from the file hangman_art.py

# ### TODO-3: 
# - Import the `logo` from hangman_art.py and print it at the start of the game.

# ### TODO-4: 
# - If the user has entered a letter they've already guessed, print the letter and let them know.
# - We should not deduct a life for this.
# - e.g. You've already guessed a

# ### TODO-5: 
# - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
# - e.g. You guessed d, that's not in the word. You lose a life.

# ### TODO-6: 
# - Update the code below to tell the user how many lives they have left.
# ```print("****************************<???>/6 LIVES LEFT****************************")```

# ### TODO 7: 
# - Update the print statement to give the user the correct word they were trying to guess.
# - e.g. `IT WAS <Correct Word>! YOU LOSE`