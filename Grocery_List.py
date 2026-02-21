def add_item(grocery_list, item):
    grocery_list.append(item)
    print(f"'{item}' has been added to the list.")


def remove_item(grocery_list, item):
    if item in grocery_list:
        grocery_list.remove(item)
        print(f"'{item}' has been removed from the list.")
        return True
    else:
        print(f"'{item}' is not in the list.")
        return False


def main():
    
    grocery_list = []

    while True:
        print("\n Grocery List Menu:")
        print("1. Add an item to the list")
        print("2. Remove an item from the list")
        print("3. View the current grocery list")
        print("4. Clear the grocery list")
        print("5. Exit the program")

        option = input("\n Please pick which choice you want(1-5):")

        if option == "1":
            list=input("What item would you like to add?")
            grocery_list.append(list)

        elif option == "2":
            list=input("What item do you want to remove?")
            if list in grocery_list:
                grocery_list.remove(list)
            else:
                print("'{item}' is not in the list.")

        elif option == "3":
            print("Viewing the current list")    
            if not grocery_list:
                print("The list is empty")
            else:
                print(grocery_list)

        elif option == "4":
            print("Clearing the list")
            grocery_list.clear

        elif option == "5":
            print("Leaving the program")
            break
    
        else:
            print("Invalid option. Please choose a number between 1 and 5")

if __name__ == "__main__":
    main()
