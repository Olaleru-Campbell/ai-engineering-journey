##Shopping List Manager - Add, remove, view items
## The user should be able to Add item, Remove item, View list and Exit
##Define separate functions for add_item(), remove_item(), view_list(), and display_menu()
##Then take their input and act based on their choice
##How will the user interact? We’ll show them a menu repeatedly (loop), like:
##What do you want to do?( Add item, Remove item, View list, Exit)
##Then take their input and act based on their choice.
##The program needs to run continuously until the user decides to stop. - 
##Decision: Use a while True loop to keep the program running and present the menu after
## each action. Use an if/elif/else structure to handle the user's menu choice.
## What logic happens in each case?
##Add item:(Ask user for the item name, Append it to the list)
##Remove item:(Ask user which item to remove, Remove it from the list (if it exists))
##View list:(Print all items, If list is empty, show “Your list is empty”)
##Exit:(Break out of the loop)

##The shopping listss232
shopping_list = []

##Display menu
def display_menu():
    print("\n---Shopping List Manager---")
    print("1. Add Item")
    print("2. View list")
    print("3. Remove Item")
    print("4. Exit")
    print("-" * 28)

##view list
def view_list():
    ## Check for empty list
    if not shopping_list:
        print("Your shopping list is empty!")
        print("Try adding some items first.")
        return
    
    print("\n--- Current Shopping List ---")
    ##Iterate and Display Items
    for i, item in enumerate(shopping_list):
        ### Output: Prints the item number (index + 1 for user readability) and the item itself.
        print(f"{i + 1}. {item}")
    print("-----------------------------")

##Add_item
def add_item():
    """Add a new item to the shopping list"""
    item_name = input("Enter item name: ").strip().capitalize()

    if item_name == "":
        print("Item cannot be empty")
        print("Try typing something")
        return
    shopping_list.append(item_name)
    ##prints a success message
    print(f"✅ '{item_name}' added to the list.")


##remove_item
def remove_item():
    """Remove an item from the shopping list (by name or number)"""
    if not shopping_list:
        print("Your list is empty, nothing to remove.")
        return
    
    ## Show the current list first
    view_list()

    user_choice= input("Enter the item name or number to remove: ").strip()

    if user_choice == "":
        print("You didn't type anything")
        return
    if user_choice.isdigit():
        ##Convert it to an actual number
        number = int(user_choice)
        ## To Validate that the chosen number is within the valid range (1 through the length of the list).
        if 1 <= number <= len(shopping_list):
            ##Remove the item
            removed_item = shopping_list.pop(number - 1)
            print(f"{removed_item} has been removed from your list.")
        else:
            print(f"Invalid number! Please choose between 1 and {len(shopping_list)}")
    else:
        item_to_remove = user_choice.capitalize()

        if item_to_remove in shopping_list:
            shopping_list.remove(item_to_remove)
            print(f"{item_to_remove} has been removed successfully")
        else:
            print(f"{item_to_remove} not found in your list")

"""Main program for shopping list manager"""
def main():
    ##Welcome message
    print("====================================")
    print("   🛍️  Welcome to Shopping List Manager!")
    print("   Let's manage your shopping list easily.")
    print("====================================\n")

    ##The while loop - “keep repeating forever” — until something stops it.
    while True:
        ##show menu
        display_menu()
        ##Get user choice
        choice = input("Choose an option (1 to 4): ").strip()
    ##Checks what the user chose and performs the correct action.
        if choice == "1":
            add_item()
        
        elif choice == "2":
            view_list()

        elif choice == "3":
            remove_item()

        elif choice == "4":
            print("\n👋 Thank you for using Shopping List Manager!")
            print("Have a great day! 🛒")
            break

        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 4.\n")



# Start the program
##“If this Python file is being run directly by you (not imported from somewhere else), then start the program by calling main().
if __name__ == "__main__":
    main()



