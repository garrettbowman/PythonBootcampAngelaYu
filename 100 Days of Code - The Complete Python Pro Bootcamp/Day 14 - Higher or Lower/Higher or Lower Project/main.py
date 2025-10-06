import random
import art
import game_data

        # 'name': 'Cardi B',
        # 'follower_count': 67,
        # 'description': 'Musician',
        # 'country': 'United States'


def comparefollowers(i1,i2):

    if int(game_data.data[i1]["follower_count"]) > int(game_data.data[i2]["follower_count"]):
        return True
    else:
        return False

used = []
continueplaying = True
first = random.randint(0,len(game_data.data)-1)

while len(used) < len(game_data.data):
    while continueplaying:
        print(art.logo)

        print()
        second = random.randint(0,len(game_data.data)-1)
        while second in used:
            second= random.randint(0,len(game_data.data)-1)
        
        print(f"A:{game_data.data[first]["name"]} " + art.vs)
        # print(art.vs)
        print(f"B:{game_data.data[second]["name"]}\n")
        print(f"Who do you think has more followers?")

        userguess= input("Type A or B:\n").lower()

        if comparefollowers(first,second) and userguess == "a":
            print(f"You were right! {game_data.data[first]["name"]} has more followers with a total of {game_data.data[first]["follower_count"]}m as opposed to {game_data.data[second]["name"]} with only {game_data.data[second]["follower_count"]}m.")
        elif not comparefollowers(first,second) and userguess == "b":
            print(f"You were right! {game_data.data[first]["name"]} has more followers with a total of {game_data.data[first]["follower_count"]}m as opposed to {game_data.data[second]["name"]} with only {game_data.data[second]["follower_count"]}m.")
        else:
            print(f"You guessed incorrectly. {game_data.data[first]["name"]} has fewer followers with a total of {game_data.data[first]["follower_count"]}m as opposed to {game_data.data[second]["name"]} with {game_data.data[second]["follower_count"]}m.")

        playagain = input("Play again? y or n:").lower()
        if playagain != "y":
            continueplaying = False
        else:
            if comparefollowers(first,second):
                used.append(second)
            else:
                used.append(first)
                first = second
    print("goodbye")
    break
