import random

from art import logo

#cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
cards = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
# cards = {
#     "A": [1,11],
#     2: 2,
#     3: 3,
#     4: 4,
#     5: 5,
#     6: 6,
#     7: 7,
#     8: 8,
#     9: 9,
#     10:10,
#     "J": 10,
#     "Q": 10,
#     "K": 10,
# }

def displayhands(player, dealer):
        
    print(f"Your's cards: ")
    for card in range(0,len(player)):
        print(player[card])
    
    print(f"Dealer's cards: ")
    print(dealer[0])
    for card in range(0,len(dealer)-1):
        print("X")

def displayhandsfinal(player, dealer):
        
    print(f"Your cards: ")
    for card in range(0,len(player)):

        print(player[card])
    
    print(f"Dealer's cards: ")
    for card in range(0,len(dealer)):

        print(dealer[card])

# def over21(hand):
#     total = 0
#     for card in hand:
#         total += cards[card].value

#     print(total)
#     if total > 21:
#         return True
#     else:
#         return False

def dealerDraw(dealer):
    if sum_cards(dealer) < 17:
        return True
    else:
        return False

def sum_cards(hand):
    subtotal = 0
    reorganize(hand)
    # for card in range(0,len(hand)-1):
    for card in range(len(hand)):
        if hand[card] in  ["J", "Q", "K"]:
            subtotal += 10
        elif hand[card] == "A":
            if subtotal > 11:
                subtotal += 1
            else:
                subtotal += 11
        else:
            subtotal += hand[card]
    return subtotal
    
def isGameover(player,dealer):
    reorganize(player)
    reorganize(dealer)
    ptotal= sum_cards(player)
    dtotal = sum_cards(dealer)
    if ptotal > 21:
        # if 11 in player:
        #     return False
        # else:
        return True
    if ptotal == 21:
        return True
    if dtotal > 21:
        # if 11 in player:
        #     return False
        # else:
        return True
    else:
        return False

# def playAgain():
#         playagain = input("Play again? y or n: ")
#         if playagain == "y":
#             blackjack()

def reorganize(hand):
    aces = hand.count("A")
    hand[:] = [card for card in hand if card != "A"] + ["A"] * aces

def blackjack():
    '''A simple blackjack game'''
    print(logo)
    continueplaying = True
    gameover = False
    player = []
    dealer = []
    #first iteration
    playerdraw = random.choice(cards)
    player.append(playerdraw)
    dealerdraw = random.choice(cards) 
    dealer.append(dealerdraw)
    
    while continueplaying:

        playerdraw = random.choice(cards)
        player.append(playerdraw)
        reorganize(player)
        dd = dealerDraw(dealer)
        if dd:
            dealerdraw = random.choice(cards) 
            dealer.append(dealerdraw)
            reorganize(dealer)
        # playerdraw = random.randint(0,12)
        # dealerdraw = random.randint(0,12)




        
        # print(f"\nYou: {playerdraw}")
        # print(f"Dealer: {dealerdraw}")
        gameover = isGameover(player,dealer)
        if gameover:
            print("GAME OVER")
            displayhandsfinal(player,dealer)
            if sum_cards(player) == 21:
                print("21! You win!")
                playagain = input("Play again? y or n: ").lower()
                if playagain == "y":
                    blackjack()
                else:
                    return

            elif sum_cards(dealer) > 21:
                if sum_cards(player) <= 21:
                    print(f"Your score is: {sum_cards(player)}")
                    print(f"The dealer's score is: {sum_cards(dealer)}")            
                    print("Dealer went over 21. You win!")
                    playagain = input("Play again? y or n: ").lower()
                    if playagain == "y":
                        blackjack()
                else:
                    return
            else:
                print(f"Your score is: {sum_cards(player)}")

                print(f"The dealer's score is: {sum_cards(dealer)}")
                print ("You lose")
                playagain = input("Play again? y or n: ").lower()
                if playagain == "y":
                    blackjack()
                else:
                    return
        else:
            displayhands(player,dealer)
        drawagain = input("\nDraw again? y or n: \n")

        if drawagain == "y":
            print("\n" *100)
            continue
        else:
            total = sum_cards(player)
            dtotal = sum_cards(dealer)
            displayhandsfinal(player,dealer)

            print(f"Your score is: {sum_cards(player)}")

            print(f"The dealer's score is: {sum_cards(dealer)}")

            if total > dtotal:
                print("You win")
            elif total == dtotal:
                print("Draw")
            else:
                print("You lose")

        playagain = input("Play again? y or n: ")
        if playagain == "y":
            blackjack()
        else:
            return

blackjack()
print("Thanks for playing! \nGoodbye")
