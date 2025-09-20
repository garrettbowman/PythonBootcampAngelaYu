import random

randominteger = random.randint(0, 1)
print(randominteger)

randomfloat = random.uniform(1,10)
print(randomfloat)

userinput = input("heads or tails")

if randominteger == 1:
    if userinput == "heads":
        
            print("heads, you win")
    else:
        print("heads, you lose")

else:
    if userinput == "tails":
        print("tails, you win")
    else:
        print("tails, you lose")