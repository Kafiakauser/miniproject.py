#CafeMenu Management

#define the menu of restaurant

menu = {
    'Pizza':120, 
    'Pasta':60,
    'Burger':70,
    'Hot dog':50,
    'Noodles':70,
    'Sandwitch':80,
    'Salad':60,
    'Coffee':100
}

#Greet
print("Welcome to PYTHON RESTAURANT!")
print("Pizza:Rs120\nPasta:Rs60\nBurger:Rs70\nHot dog:Rs50\nNoodles:Rs70\nSandwitch:Rs80\nSalad:Rs60\nCoffee:Rs100")

order_total = 0

item_1=input("Enter the name of the item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]   #0 + 50
    print(f"your iten {item_1} has added to your order")

else:
    print(f"your order {item_1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No): ")
if another_order == "Yes":
    item_2 = input("Enter the name of the second item = ")
    if item_2 in menu:
        order_total += menu[item_2]   
        print(f"your iten {item_2} has added to your order")

    else:
        print(f"your order {item_2} is not available")

print(f"Total ampunt to pay is {order_total}")
