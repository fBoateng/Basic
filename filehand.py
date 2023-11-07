def read_menu(filename):
    f = open(filename)
    temp = f.readlines()
    result = []
    for item in temp:
        result.append(item.strip())
    f.close()
    return result

drinks = read_menu('drinks.txt')
print(drinks)
flavor = read_menu('flavor.txt')
print(flavor)
toppings = read_menu('toppings.txt')
print(toppings)
