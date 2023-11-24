# c:/Users/se/Desktop/Basic/first_app.py

import json
import os

from flask import Flask, render_template, request


def save_orders(orders, filename):
    f = open(filename, "w")
    json.dump(orders, f, indent=4)
    f.close()
    return

def load_orders(filename):
    if os.path.exists(filename):
        f = open(filename, "r")
        orders = json.load(f)
        f.close()
        return orders
    else:
        orders = []
        return orders

orders = load_orders("orders.json")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello/<name>")
def greet(name="Stranger"):
    return render_template("greeting.html", name=name)

@app.route("/order", methods=("GET", "POST"))
def order():
    if request.method == "POST":
        new_order = {"name": request.form["name"],
                     "drink": request.form["drink"],
                     "flavor": request.form["flavor"],
                     "topping": request.form["topping"]
                     }
        orders.append(new_order)
        save_orders(orders, "orders.json")
        return render_template(
            "print.html", new_order=new_order
        )
        
        
        
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

    return render_template("forms.html")

if __name__ == '__main__':  
   app.run()