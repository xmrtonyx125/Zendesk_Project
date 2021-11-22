
class Menu():
    def __init__(self) -> None:
        pass

    def printMenu(self):
        print("Select view options:")
        print(" * Press 1 to view all tickets")
        print(" * Press 2 to view a ticket")
        print(" * Type 'quit' to exit\n")
        

    def exit_Prompt(self):
        print("*" * 38)
        print("*    Thank you for using the viewer  *")
        print("*         Have a good day            *") 
        print("*" * 38)

    def welcome_Prompt(self):
        print("\n")
        print("*" * 49)
        print("*        WELCOME TO THE TICKET VIEWER           * ")
        print("*  Type 'menu' to view option or 'quit' to exit * ")
        print("*" * 49)

    def login_Prompt(self):
        print("Enter your Zendesk account")
        email = input ("Email: ")
        password = input("Password: ")
        return email, password
    
    def status_401(self):
        print("-" * 41)
        print("|   Couldn't authentical you. Code 401  |")
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