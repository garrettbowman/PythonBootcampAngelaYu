#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./input/letters/starting_letter.txt") as start:
    start_letter = start.read()
    print(start_letter)
with open("./input/Names/invited_names.txt") as names:
    num_names = names.readlines()
    print(num_names)
    names = []
    for name in range(len(num_names)):
        names.append(num_names[name].strip("\n"))

    print(names)
for name in range(len(names)):
    # names += num_names[name].strip("n","/","\""",")

    new_letter =start_letter.replace("[name]", names[name])
    print(new_letter)
    print(names)
    with open(f"./Output/ReadyToSend/Letter_for_{names[name]}.txt", mode="w") as out:
        out.write(new_letter)
