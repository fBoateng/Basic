def main_menu():
    while True:
        order = get_order()
        print('Check your order:')
        print(order)
        confirm = input('Confirm? Press Y to confirm, N to cancel: ').capitalize
        save_order(order)
        print('Thanks for your order!')
        print_order(order)
        

def menu(choices, title, prompt):
    print(title)
    print('-' *  len(title))
    i = 1
    for c in choices:
        print(i, c)
        i += 1
    while True:    
        choice = input(prompt)
        allowed_answers = []
        for a in range(1, len(choices) + 1):
            allowed_answers.append(str(a))
            allowed_answers.append('X')
            allowed_answers.append('x')
        if choice in allowed_answers:
            if choice == 'X' or choice == 'x':
                answer = ''
                break
                
            else:
                answer = choices[int(choice) - 1]
        
                break
        else:
            print('Enter a number from 1 to', len(choices))
            answer = ''
        
    
    return answer


def read_menu(filename):
    f = open(filename)
    temp = f.readlines()
    result = []
    for item in temp:
        result.append(item.strip())
    f.close()
    return result


def get_order():
    order = {}
    order['name'] = input('What is your name: ').capitalize()
    drinks = read_menu('drinks.txt')
    flavor = read_menu('flavor.txt')
    toppings = read_menu('toppings.txt')
    drink = menu(drinks, 'What drink would you like?', 'Enter a number: ')
    flavor = menu(flavor, 'What flavor would you like?', 'Enter a number: ')
    toppings = menu(toppings, 'What toppings would you like?', 'Enter a number: ')
    order['drink'] = drink
    order['flavor'] = flavor
    order['toppings'] = toppings
    return order


def print_order(order):
    print("Here is your order, ", order["name"])
    print("Main product: ", order["drink"])
    print("Flavor: ", order["flavor"])
    print("Topping: ", order["toppings"])
    print("Thanks for your order!")
    return

def save_order(order):
    print('Saving order...')
    return


main_menu()