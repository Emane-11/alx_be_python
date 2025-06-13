def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # ✅ Checks for implementation of an array shopping_list
    shopping_list = []

    while True:
        # ✅ Checks for calling display_menu function
        display_menu()

        # ✅ Checks for implementation of Choice Input as a number
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in your shopping list.")
        elif choice == 3:
            if not shopping_list:
                print("Your shopping list is currently empty.")
            else:
                print("Your Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

