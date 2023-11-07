def menu(choices, title, prompt):
    print(title)
    print('-' *  12)
    i = 1
    for c in choices:
        print(i, c)
        i += 1
    choice = int(input(prompt))
    answer = choices[int(choice) - 1]
    
    return answer


drinks = ["chocolate", "coffee", "decaf"]
flavors = ["caramel", "vanilla", "peppermint", "raspberry", "plain"]
toppings = ["chocolate", "cinnamon", "caramel"]

drink = menu(drinks, "Erik's Coffee Shop drinks", "Choose your drink: ")
flavor = menu(flavors, "Erik's Coffee Shop flavors", "Choose your flavor: ")
topping = menu(toppings, "Erik's Coffee Shop toppings", "Choose your topping: ")

print("Here is your order: ")
print("Main product: ", drink)
print("Flavor: ", flavor)
print("Topping: ", topping)
print("Thanks for your order!") 



    
    