import random
import art
import game_data


print(art.logo)

continueplaying = True

while continueplaying:
    i = random.randint(0,len(game_data.data))
    print(i)
    print(f"")