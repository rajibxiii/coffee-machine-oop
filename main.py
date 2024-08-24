from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from sys import exit, stdout
from time import sleep
from os import system

coffe_maker_object = CoffeeMaker()
money_machine_object = MoneyMachine()
menu_object = Menu()

def wait (waitingTime):
    for i in range (waitingTime, 0, -1):
        stdout.write (f"\rNext order in {i} seconds") #temporary print
        stdout.flush() #deleting temporary print
        sleep (1)

machine_on = True
while (machine_on):
    availableCoffe = menu_object.get_items()
    prompt = input (f"What would you like? ({availableCoffe}): ")
    
    if prompt == 'off':
        machine_on = False
    elif prompt == 'report':
        coffe_maker_object.report()
        money_machine_object.report()
    elif (prompt == 'espresso' or prompt == 'latte' or prompt == 'cappuccino'):
        itemToOrder = menu_object.find_drink(prompt) #searching item
        if (itemToOrder): #checking if item is available
            if(coffe_maker_object.is_resource_sufficient(itemToOrder)):
                priceOfDrink = itemToOrder.cost
                if (money_machine_object.make_payment(priceOfDrink)):
                    coffe_maker_object.make_coffee(itemToOrder)
                    wait(5)
                    system('cls')
    else:
        print("Wrong input. Enter again.")
        wait(5)
        system('cls')

exit("Machine turned off.")