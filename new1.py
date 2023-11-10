# drink_options = ["chocolate", "coffee", "decaf"]
# flavor_options = ["caramel", "vanilla", "peppermint", "raspberry", "plain"]
# topping_options = ["chocolate", "cinnamon", "caramel"]

# print("Erik's Coffee Shop drinks")
# print("-------------------------")
# i = 1
# for d in drink_options:
#     print(i, d)
#     i += 1
# drink = input("Choose your drink: ")

# print("Erik's Coffee Shop flavors")
# print("--------------------------")
# i = 1
# for f in flavor_options:
#     print(i, f)
#     i += 1
# flavor = input("Choose your flavor: ")

# print("Erik's Coffee Shop toppings")
# print("---------------------------")
# i = 1
# for t in topping_options:
#     print(i, t)
#     i += 1
# topping = input("Choose your topping: ")

# print("Your order is: ", )
# print('Main drink: ', drink_options[int(drink) - 1])
# print('Flavor: ', flavor_options[int(flavor) - 1])
# print('Topping: ', topping_options[int(topping) - 1])



# def pizza_menu(choices, title, prompt):
#     print(title)
#     print('-' *  len(title))
#     i = 1
#     for c in choices:
#         print(i, c)
#         i += 1
#     choice = int(input(prompt))
#     answer = choices[int(choice) - 1]
    
#     return answer


# food = ['pizza', 'pasta', 'salad', 'soup']
# toppings = ['pepperoni', 'ham', 'mushrooms', 'onions']
# sauces = ['marinara', 'alfredo', 'bbq', 'tomato']
# drinks = ['coffee', 'chocolate', 'lemonade', 'ice tea']


# meal = pizza_menu(food, 'What would you like?', 'Enter a number: ')
# topping = pizza_menu(toppings, 'What toppings would you like?', 'Enter a number: ')
# sauce = pizza_menu(sauces, 'What sauce would you like?', 'Enter a number: ')
# drink = pizza_menu(drinks, 'What drink would you like?', 'Enter a number: ')

# print("Here is your order: ")
# print("Main product: ", meal)
# print("Sauce: ", sauce)
# print("Topping: ", topping)
# print("Drink: ", drink)
# print("Thanks for your order!") 


import json

order = {
"name": "Erik",
"drink": "coffee",
"flavor": "caramel",
"topping": "chocolate"
}


order1 = {
    "name": "Alex",
    "drink": "chocolate",
    "flavor": "vanilla",
    "topping": "caramel",
}

orders = []

orders.append(order)
orders.append(order1)


f = open("orders.json", "w")
json.dump(order, f, indent=4)
f.close()


save_order = []
f = open("orders.json", 'r')
save_order = json.load(f)
print(save_order)