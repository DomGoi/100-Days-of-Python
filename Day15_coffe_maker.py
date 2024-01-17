LOGO='''
                        (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /\                             /
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
  jgs \""--..__                              __..--""/
       '._     """----.....______.....----"""     _.'
          `""--..,,_____            _____,,..--""`
                        `"""----"""`'''
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
    'money $':0
}
#Function for order
def order(order):
    '''Evaluates wether there is an appropriate amount of ingridients and after payment deduce them from resources.'''
    water_needed = int(MENU[order]['ingredients'].get('water', 0))
    milk_needed = int(MENU[order]['ingredients'].get('milk', 0))
    coffee_needed = int(MENU[order]['ingredients'].get('coffee', 0))
    if int(resources['water']) < water_needed:
        res_text="Not enough water. Please refill"
        return res_text

    if int(resources['milk']) < milk_needed :
        res_text ="Not enough milk. Please refill"
        return res_text

    if int(resources['coffee']) < coffee_needed:
        res_text="Not enough coffee. Please refill"
        return res_text

    text, money_in, resources_money = money(user_input)
    print(text)
    if text == "Sorry insufficient funds. Money refunded.":
            pass
    else:
        resources['water'] -= water_needed
        resources['milk'] -= milk_needed
        resources['coffee'] -= coffee_needed
        return None

def money(user_input):
    '''Function calculate wether sum of value of inserted coins is enough for paying for the drink or not.'''
    print("Please insert coins")

    pen=float(input('How many pennies? (input number)'))

    nic=float(input('How many nickles? (input number)'))
    dim=float(input('How many dimes? (input number)'))
    quar=float(input('How many quarters ?(input number)'))
    money_in=0.01*pen+nic*0.05+0.10*dim+0.25*quar
    if money_in > float(MENU[user_input]['cost']):
        rest=money_in-float(MENU[user_input]['cost'])
        resources['money $']=float(MENU[user_input]['cost'])
        text=f"Here is {round(rest,2)} $ in change.Hers is you {user_input}."
        return text, money_in, resources['money $']

    elif money_in == float(MENU[user_input]['cost']):
        resources['money $'] = float(MENU[user_input]['cost'])
        text=(f"Thank you, funds are sufficient."
              f"Here is you {user_input}.")
        return text, money_in, resources['money $']

    elif money_in < float(MENU[user_input]['cost']):
        text="Sorry insufficient funds. Money refunded."
        end_text="End"
        return text, money_in, resources['money $']

    else:
        text="Something is wrong."
        return text, money_in


def report():
    '''Show report of the resources, available'''
    resources_re = f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee:{resources['coffee']} \nMoney:{resources['money $']}"
    return resources_re


def off():
    '''Shut down the coffe maker.'''
    prog_run = False
    off_text='Turning off.'
    return off_text

print(LOGO)
coffee_on = True

while coffee_on:
    user_input = input('What would you like to order? espresso/cappuccino/latte').lower().strip()

    if user_input == 'espresso' or user_input == 'cappuccino' or user_input == 'latte':
        res_text=order(user_input)
        if res_text:
            print(res_text)
            coffee_on=False


    elif user_input == 'off':
        off_text = off()
        if off_text == 'Turning off.':
            coffee_on = False

    elif user_input == 'report':
        report_res = report()
        print(report_res)
        continue
    else:
        print("Wrong input. Please try again.")
        continue
