art = '''
    (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \ 
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \ 
\_____________________/
'''



MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def calculatecoins(q,d,n,p):
    '''returns total from coins as argument q d n p'''
    return round(q *0.25 + d * 0.1 + n *0.05 + p *0.01,2)

def makereport():
    '''prints report'''
    for key in resources:
        print(f"{key.capitalize()}: {resources[key]}\n")

def makebev(item,money):
    global resources
    
    if item == "1":
        iorder = "espresso"
    elif item == "2":
        iorder = "latte"
    else:
        iorder = "cappuccino"

    for key in MENU[iorder]["ingredients"]:
       # resources[key] -= MENU[iorder]["ingredients"][key]
       resources[key] = resources[key] - MENU[iorder]["ingredients"][key]

    print(f"\nEnjoy your beverage!\nYour change is {money - MENU[iorder]["cost"]}\nNext Customer!")

def canmakebev(item):
    '''is there enough resources true or false'''
    if int(item) == "1":
        iorder = "espresso"
    elif int(item) == "2":
        iorder = "latte"
    else:
        iorder = "cappuccino"

    for key in MENU[iorder]["ingredients"]:
        if resources[key] - MENU[iorder]["ingredients"][key] <0:
            return False
    return True

def enough(order,money):
    if int(order) == "1":
        iorder = "espresso"
    elif int(order) == "2":
        iorder = "latte"
    else:
        iorder = "cappuccino"

    return money > MENU[iorder]["cost"]

on = True

while on:

    # print(MENU["latte"]["ingredients"])

    # makereport()
    order = input(f"Welcome to the Coffee Shop!{art} \nWhat would you like to order? \n1-espresso ${MENU["espresso"]["cost"]} \n2-latte ${MENU["latte"]["cost"]}\n3-cappuccino ${MENU["cappuccino"]["cost"]}\n4-report\n")
    if order == "4":
        makereport()
    else:
        if canmakebev(order): 
            quarters = int(input("How many quarters would you like to insert?"))
            dimes = int(input("How many dimes would you like to insert?"))
            nickels = int(input("How many nickels would you like to insert?"))
            pennies = int(input("How many pennies would you like to insert?"))


            inserted = calculatecoins(quarters, dimes, nickels, pennies)
            print(f"You inserted ${inserted}")
            # print(calculatecoins(1,2,3,4))
            if enough(order, inserted):
                makebev(order,inserted)
            else:
                print("You need to insert more money.")
                while not enough(order, inserted):
                    inserted += float(input("How much more money would you like to insert?"))
                makebev(order, inserted)
            # makereport()
        else:
            print("\nsorry, come back later\n")
