def read_menu(filename):
    f = open(filename)
    temp = f.readlines()
    result = []
    for item in temp:
        new_item = item.strip()
        result.append(new_item)
    return result

def get_order():
    order = {}
    name = input("Enter your name or enter 'X' to exit: ")
    if name == 'x'.capitalize() or name == 'X':
        return {}
    else:
        order["name"] = name
    drinks = read_menu('drinks.txt')
    flavors = read_menu('flavors.txt')
    toppings = read_menu('toppings.txt')
    order["drink"] = menu(drinks, 'Erik\'s drinks', 'Choose your drink: ')
    order["flavor"] = menu(flavors, 'Erik\'s flavors', 'Choose your flavor: ')
    order["topping"] = menu(toppings, 'Erik\'s toppings', 'Choose your topping: ')
    return order


def print_order(order):
    print("Here is your order, ", order["name"])
    print("Main product: ", order["drink"])
    print("Flavor: ", order["flavor"])
    print("Topping: ", order["topping"])
    print("Thanks for your order!")
    return