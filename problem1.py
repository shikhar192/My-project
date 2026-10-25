items = []  
while True:
    print("welcome to the Cafe Management System")
    print("----------------------")
    print("1. Add Item")
    print("2. Display Items")
    print("3. Search Items")
    print("4. Exit")
    choice = int(input("Enter your choice:"))
    print("----------------------")

    if choice ==1:
        item_name = input("enter item name:")
        item_price = int(input("enter item price:"))
        items.append((item_name, item_price))
        print(f"Item added: {item_name} with price {item_price}")
        print("Item added successfully!")

    elif choice ==2:
        print("Displaying items...")
        # Code to display items goes here
        for item_name, item_price in items:
            print(f"Item[{item_name}] = ${item_price}")
    elif choice ==3:
        print("Searching items...")
        # Code to search items goes here
        search_name = input("Enter the item name to search:")
        found_items = [item for item in items if item[0] == search_name]
        for item_name, item_price in found_items:
            print(f"Item found: {item_name} - price${item_price}")
        if not found_items:
            print("Item not found.")
        

    elif choice ==4:
        print("Exiting...Menu")
        print("Thank you for using the Cafe Management System!")
        break
        # Code to exit the program goes here


    else:   
        print("Invalid choice. Please try again.")


