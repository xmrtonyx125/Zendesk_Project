from menu import Menu
from API_call import API


menu = Menu()
api = API()

api.get_Data()
menu.welcome_Prompt()
user_input  = input ("Your input: ")
print("\n")
if user_input == 'menu':
    
    menu.printMenu()
    menu_input = input ("Your input: ")
    while (menu_input != 'quit') and (menu_input != 'exit'): # Loop until user type quit or exit
        if (menu_input != '1' and menu_input != '2'): # user enter something not in the menu's option
            print("Please choose from the menu")
            print("\n")






        menu.printMenu()
        menu_input = input ("Your input: ")


    menu.exit_Prompt() # Good-bye message


elif user_input ==  'quit' or 'exit': # exiting 
    menu.exit_Prompt()  # Good-bye message
