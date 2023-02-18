

menu = {"pizza": 4.00,
        "nachos": 3.25,
        "chips": 2.00,
        "candy": 2.25,
        "water": 1.00,
        "italian soda": 2.50,
        "pretzel" : 3.00,
        "popcorn": 2.50}

cart = []
total = 0
print("-------menu-------")
for key, value in menu.items():
    print(f"{key}: ${value:.2f}")
print("-------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(f"{menu.get(food):2} {food}")
print(f"Total is: ${total}")
