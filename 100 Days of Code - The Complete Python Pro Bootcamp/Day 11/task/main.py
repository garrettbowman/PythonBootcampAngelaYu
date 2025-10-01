import random

from art import logo

cards = {
    "A": [1,11],
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10:10,
    "J": 10,
    "Q": 10,
    "K": 10,
}
def over21(hand):
    total = 0
    for card in hand:
        total += cards[card].value

    print(total)
    if total > 21:
        return True
    else:
        return False

def draw(player):
    # later
    return
    
    
def blackjack():
    '''A simple blackjack game'''
    print(logo)
    continueplaying = True
    player = []
    dealer = []
    while continueplaying:

        playerdraw = random.choice(cards)
        dealerdraw = random.choice(cards)

        # playerdraw = random.randint(0,12)
        # dealerdraw = random.randint(0,12)
        player.append(playerdraw)
 
        dealer.append(dealerdraw)

        print(f"You: {playerdraw}")
        print(f"Dealer: {dealerdraw}")

        drawagain = input("\nDraw again? y or n: ")

        if drawagain == "y":
            continue
        else:
            total = 0
            dtotal = 0
            for card in player:
                total += int(cards[card])
            print(f"Your score is : {total}")

            for card in dealer:
                dtotal += cards[card]
            print(f"The dealer's score is: {dtotal}")

        playagain = input("Play again? y or n: ")
        if playagain == "y":
            blackjack()

        else:
            return

blackjack()
print("Goodbye")
