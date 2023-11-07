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

drinks = read_menu('drinks.txt')
flavor = read_menu('flavor.txt')
toppings = read_menu('toppings.txt')



drink = menu(drinks, "Erik's Coffee Shop drinks", "Choose your drink: ")
flavor = menu(flavor, "Erik's Coffee Shop flavors", "Choose your flavor: ")
topping = menu(toppings, "Erik's Coffee Shop toppings", "Choose your topping: ")

print("Here is your order: ")
print("Main product: ", drink)
print("Flavor: ", flavor)
print("Topping: ", topping)
print("Thanks for your order!") 



    
    