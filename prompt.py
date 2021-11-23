
class Menu():
    def __init__(self) -> None:
        pass

    def printMenu(self):
        print("*" * 37)
        print("Select view options:                *")
        print(" * Press 1 to view all tickets      *")
        print(" * Press 2 to view a ticket         *")
        print(" * Type 'quit' to exit              *")
        print("*" * 37)


    def exit_Prompt(self):
        print("*" * 38)
        print("*    Thank you for using the viewer  *")
        print("*         Have a good day            *") 
        print("*" * 38)

    def error_option(self):
        print("\n")
        print("*" * 33)
        print("*  Please choose from the menu  *")
        print("*" * 33)
        print("\n")
        
    def welcome_Prompt(self):
        print("\n")
        print("*" * 49)
        print("*        WELCOME TO THE TICKET VIEWER           * ")
        print("*  Type 'menu' to view option or 'quit' to exit * ")
        print("*" * 49)
        user_input  = input ("Your input: ") #type menu or quit
        return user_input

    def login_Prompt(self):
        print("Enter your Zendesk account")
        subdomain = input("Subdomain: ")
        email = input ("Email: ")
        password = input("Password: ")
        return subdomain, email, password
    
    def status_401(self):
        print("-" * 41)
        print("|   Couldn't authenticate you. Code 401 |")
        print("| The username or password is incorrect |")
        print("-" * 41)
    
    
    def status_200(self):
        print("-" * 41)
        print("|           ACCESS GRANTED              |")
        print("-" * 41)

    def status_500 (self):
        print("*" * 15)
        print("Internal Server Error. Code 500 *")
        print("*" * 15)

    def all_tickets_prompt(self):
        print("*" * 54)
        print("*    ALL TICKETS LOADED. Choose from options below   *")
        print("*    Press 1 or 'next' to view the next page         *")
        print("*    Press 2 or 'prev' to view the previous page     *")
        print("*    Press 3 or 'home' to return to main page        *")
        print("*    Type 'quit' to exit                             *")
        print("*" * 54)

    def a_ticket_prompt(self):
        print("*" * 45)
        print("*           Search again (yes/no):          *")
        print("* Press 3 or 'home' to return to main page  *")
        print("*" * 45)

    def display(self):
        print(f"Ticket ID   Subject { ' ' * 45} Created At { ' ' * 15} Assigned By")
        print("_" * 120)