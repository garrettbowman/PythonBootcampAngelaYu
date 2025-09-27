import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

chosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()

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