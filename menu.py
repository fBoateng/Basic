# drinks = ['coffee', 'chocolate', 'decafe', 'tea']
# flavors = ['vanilla', 'chocolate', 'strawberry', 'plain']
# toppings = ['sprinkles', 'chocolate', 'strawberry', 'cinnamon']


# '''for d in drinks:
#     for f in flavors:
#         for t in toppings:
#             print(d, f, t)'''

# i = 1
# for d in drinks:
#     print(i, d)
#     i += 1

# i = 1            
# for f in flavors:
#         print(i, f, '---')
#         i += 1
        
# i = 0  
# for t in toppings:
#     print(i, t )
#     i += 1


def get_order():
    order = {}
    order['name'] = input('What is your name: ')
    return {}