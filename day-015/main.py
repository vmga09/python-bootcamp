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

coins = {
    "quarters": 0.25,
    "dimes":0.10,
    "nickles":0.05,
    "pennies":0.01

}

profit = 0

def report():

    print(f"""Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: ${profit} """)


def check_resources(option):
    check = True
    for item in MENU[option]["ingredients"]:
        if resources[item] < MENU[option]["ingredients"][item]:
            check = False
            print(f"Sorry there is not enough {item}.")
    return check 

def calc_money():
    print("Please insert coins.")
    quarters = int(input("How many quartes?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return round(quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01,2)


def check_pay(option,valor):
    if MENU[option]["cost"] > valor:
        print(f"Sorry valor insuficiente ")
        return False
    else:
        change = valor - MENU[option]["cost"]
        print(f"Here is ${change} in change.")
        print(f"Here is your {option} ☕️ Enjoy!")
        return True

def update_resource(option):
    for item in MENU[option]["ingredients"]:
        resources[item] -= MENU[option]["ingredients"][item]

off = False


while not off:
    client_choice = input("What would you like? (espresso/latte/cappuccino) :")
    if client_choice == "report":
        report()

    elif client_choice in MENU:
        if check_resources(client_choice):
            money = calc_money()
            if check_pay(client_choice,money):
                profit += MENU[client_choice]["cost"]
                update_resource(client_choice)
    elif client_choice == 'off':
        off = True

    else:
        print("Opcion no valida 😵‍💫")







