"""
Shopping list to cal....
author: Jun Han
"""

def get_shoppinglist():
    shopping_list = [] # it is a list that stores values.
    total_price = 0
    while True:
        item = input("Enter the name of the item (or type 'done' to finish):")
        if item.lower() == 'done':
            break
        try:
            price = float(input(f"Enter the price of  '{item}': "))
            shopping_list.append((item,price)) 
            total_price += price
        except ValueError:
            print("Invalid input. please enter a numeric value for the price.")

    return shopping_list,total_price

def main():
    print("Welcome to the shopping list program")
    shooping_list, total_price = get_shoppinglist()

    if not shooping_list:
        print("No itmes were entered")
    else:
        print("\nShopping list:")
        for item, price in shooping_list:
            print(f"{item},${price:.2f}")
        print(f"\nTotal price: ${total_price:.2f}")

main()

