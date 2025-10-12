import random
import art
import game_data

        # 'name': 'Cardi B',
        # 'follower_count': 67,
        # 'description': 'Musician',
        # 'country': 'United States'

def printaccs(one, two):
        """Formats the gama data"""
        print(f"A:\n{game_data.data[one]["name"]}\n{game_data.data[one]["country"]}\n{game_data.data[one]["description"]} " + art.vs)
        # print(art.vs)
        print(f"B:\n{game_data.data[two]["name"]}\n{game_data.data[two]["country"]}\n{game_data.data[two]["description"]} \n")
        print(f"Who do you think has more followers?")

def comparefollowers(i1,i2):
    """Grabs followercount and if first greater returns true """
    if int(game_data.data[i1]["follower_count"]) > int(game_data.data[i2]["follower_count"]):
        return True
    else:
        return False

def comparefollowers2(userguess, followercount1, followercount2):
    """Grabs followercount and if first greater returns true """
    if followercount1 > followercount2:
        return userguess == "a"
    else:
        return userguess == "b" 
used = []
continueplaying = True
first = random.randint(0,len(game_data.data)-1)

while len(used) < len(game_data.data):
    while continueplaying:
        print(art.logo)
        score = 0
        print()
        second = random.randint(0,len(game_data.data)-1)
        while second in used:
            second= random.randint(0,len(game_data.data)-1)

        printaccs(first,second)        
        # print(f"A:{game_data.data[first]["name"]} " + art.vs)
        # # print(art.vs)
        # print(f"B:{game_data.data[second]["name"]}\n")
        # print(f"Who do you think has more followers?")

        userguess= input("Type A or B:\n").lower()

        if comparefollowers(first,second) and userguess == "a":
            print(f"\nYou were right! {game_data.data[first]["name"]} has more followers with a total of {game_data.data[first]["follower_count"]}m as opposed to {game_data.data[second]["name"]} with only {game_data.data[second]["follower_count"]}m.")
            score += 1
        elif not comparefollowers(first,second) and userguess == "b":
            print(f"\nYou were right! {game_data.data[first]["name"]} has more followers with a total of {game_data.data[first]["follower_count"]}m as opposed to {game_data.data[second]["name"]} with only {game_data.data[second]["follower_count"]}m.")
            score += 1
        else:
            print(f"\nYou guessed incorrectly. {game_data.data[first]["name"]} has {game_data.data[first]["follower_count"]}m as opposed to {game_data.data[second]["name"]} with {game_data.data[second]["follower_count"]}m.")
        print(f"\nYour score is {score}")
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
