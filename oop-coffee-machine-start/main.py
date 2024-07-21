from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
choice = input("What would u like?(espresso/latte/cappuccino/):")
Menu = Menu()
x = CoffeeMaker()
money = MoneyMachine()
if choice == 'espresso':
    drink = Menu.menu[1]
elif choice == 'latte':
    drink = Menu.menu[0]
elif choice == 'cappuccino':
    drink = Menu.menu[2]
elif choice == "report":
    x.report()
y = x.is_resource_sufficient(drink)
if y and money.make_payment(drink.cost):
    x.make_coffee(drink)


