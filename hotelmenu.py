#Define The Menu Of Restaurant
menu = {
    "Pizza":40,
    "Burger":60,
    "Pasta":50,
    "Salad":70,
    "Coffee":80,
}

#Greet
print("Welcome To The Noor's Restaurant")
print("Pizza: Rs 40\nBurger: Rs 60\nPasta: Rs 50\nSalad: Rs 70\nCoffee: Rs 80\n")

order_total = 0
#80 + 70 = 150

item_1 = input("Enter The Name Of Item You Want To Order = ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 50
    print(f"Your Item {item_1} Has Been Added To Your Order")

else:
    print("Ordered Item {item_1} Is Not Available Yet!")

    another_order = input("Do You Want To Order Another Item? (Yes/No)")
    if another_order == "Yes":
        item_2 = input("Enter The Name Of Second Item = ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Your Item {item_2} Has Been Added To Your Order")
        else:
            print(f"Ordered Item {item_2} Is Not Available Yet!")

    else:
        print(f"The Total Amount Of Items To Pay Is{order_total}")