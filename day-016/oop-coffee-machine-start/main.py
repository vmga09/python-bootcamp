from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
#menu_items = MenuItem()


is_off = False
while not is_off:
    client_choice = input(f"What would you like? ({menu.get_items()}) :")
    if client_choice == "report":
        coffe_maker.report()
        money_machine.report()
    elif client_choice == "off":
        is_off = True
    else:
        ingredients = menu.find_drink(client_choice)
        if coffe_maker.is_resource_sufficient(ingredients) and money_machine.make_payment(ingredients.cost):
            coffe_maker.make_coffee(ingredients)