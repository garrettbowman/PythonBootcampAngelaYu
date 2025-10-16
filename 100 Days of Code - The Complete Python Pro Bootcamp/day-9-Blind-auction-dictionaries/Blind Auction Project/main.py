# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
bids = {}

should_continue = "yes"
while should_continue == "yes":
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))


    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if should_continue == "yes":
        print("\n" * 100)


find_highest_bidder(bids)

# for key in bids:
#     if bids[key] == max(bids.values()):
#         print(f"The winner is {key} with a bid of ${bids[key]}")