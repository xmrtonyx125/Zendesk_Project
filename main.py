from menu import Menu
from API_call import API


menu = Menu()
api = API()

return_api_code = api.get_response_code()


if (return_api_code == 401):
    menu.status_401()

elif (return_api_code == 500):
    menu.status_500()

elif (return_api_code == 200):
    menu.status_200()


    menu.welcome_Prompt()
    user_input  = input ("\nYour input: ")
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
