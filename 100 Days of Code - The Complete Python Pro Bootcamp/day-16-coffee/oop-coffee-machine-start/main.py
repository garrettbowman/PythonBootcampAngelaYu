from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

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
money_machine = MoneyMachine()
coffee = CoffeeMaker()
mymenu = Menu()
is_on = True

while is_on:
    money_machine.report()

    options = mymenu.get_items()
    print("Welcome to StarBucks!")
    order = input(f"{art} \nWhat would you like to order? {options} or report\n").lower()
    if order == "off":
        is_on = False

    elif order == "report":
        money_machine.report()
        coffee.report()

    else:
        drink =mymenu.find_drink(order)
        print(drink)
        if coffee.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee.make_coffee(drink)


