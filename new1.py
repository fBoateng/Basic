drink_options = ["chocolate", "coffee", "decaf"]
flavor_options = ["caramel", "vanilla", "peppermint", "raspberry", "plain"]
topping_options = ["chocolate", "cinnamon", "caramel"]

print("Erik's Coffee Shop drinks")
print("-------------------------")
i = 1
for d in drink_options:
    print(i, d)
    i += 1
drink = input("Choose your drink: ")

print("Erik's Coffee Shop flavors")
print("--------------------------")
i = 1
for f in flavor_options:
    print(i, f)
    i += 1
flavor = input("Choose your flavor: ")

print("Erik's Coffee Shop toppings")
print("---------------------------")
i = 1
for t in topping_options:
    print(i, t)
    i += 1
topping = input("Choose your topping: ")

print("Your order is: ", )
print('Main drink: ', drink_options[int(drink) - 1])
print('Flavor: ', flavor_options[int(flavor) - 1])
print('Topping: ', topping_options[int(topping) - 1])