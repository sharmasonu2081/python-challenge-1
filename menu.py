# Step 0: Initialize the menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Step 1: Flatten the Menu for Display
def flatten_menu(menu):
    flattened = {}
    item_number = 1
    for category, items in menu.items():
        print(f"\n{category}:")
        for item, details in items.items():
            if isinstance(details, dict):
                for subtype, price in details.items():
                    full_item_name = f"{item} - {subtype}"
                    print(f"{item_number}. {full_item_name}: ${price}")
                    flattened[item_number] = {"Item name": full_item_name, "Price": price}
                    item_number += 1
            else:
                print(f"{item_number}. {item}: ${details}")
                flattened[item_number] = {"Item name": item, "Price": details}
                item_number += 1
    return flattened

flattened_menu = flatten_menu(menu)

# Step 2: Initialize Order List
orders = []

# Step 3: Order Placement with Menu Selection by Number
while True:
    try:
        menu_selection = int(input("\nPlease enter the item number you would like to order: "))
        if menu_selection not in flattened_menu:
            print("Error: Please select a valid item number.")
            continue
    except ValueError:
        print("Error: Please enter a numeric value.")
        continue

    selected_item = flattened_menu[menu_selection]
    item_name = selected_item["Item name"]
    price = selected_item["Price"]

    quantity_input = input(f"How many of {item_name} would you like to order? (Default is 1): ")
    quantity = 1 if not quantity_input.isdigit() else int(quantity_input)

    orders.append({"Item name": item_name, "Price": price, "Quantity": quantity})

    if input("Would you like to order anything else? (Y/N): ").lower() != 'y':
        print("Thank you for your order.")
        break

# Step 4: Print the Receipt
print("\nYour receipt:\nItem name                          | Price   | Quantity")
print("-"*58)
total_price = 0
for order in orders:
    item_name, price, quantity = order["Item name"], order["Price"], order["Quantity"]
    total_price += price * quantity
    print(f"{item_name:40} | ${price:6} | {quantity}")

print(f"\nTotal: ${total_price:.2f}")
