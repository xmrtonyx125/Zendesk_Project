
class Menu():
    def __init__(self) -> None:
        pass

    def printMenu(self):
        '''
            Function priting menu to see the ticket
            Return none
        '''
        print("*" * 37)
        print("Select view options:                *")
        print(" * Press 1 to view all tickets      *")
        print(" * Press 2 to view a ticket         *")
        print(" * Type 'quit' to exit              *")
        print("*" * 37)


    def exit_Prompt(self):
        '''
            Function priting the good-bye messeage to the user
            Return none
        '''
        print("*" * 38)
        print("*    Thank you for using the viewer  *")
        print("*         Have a good day            *") 
        print("*" * 38)

    def error_option(self):
        '''
            Function printing if the input not followed the menu
            Return none
        '''
        print("\n")
        print("*" * 33)
        print("*  Please choose from the menu  *")
        print("*" * 33)
        print("\n")
        
    def welcome_Prompt(self):
        '''
            Function priting welcome messeage 
            Return non
        '''
        print("\n")
        print("*" * 49)
        print("*        WELCOME TO THE TICKET VIEWER           * ")
        print("*  Type 'menu' to view option or 'quit' to exit * ")
        print("*" * 49)

    def login_Prompt(self):
        '''
            Function prompt and ask for user input login information
            Return: input of subdomain, email, and password
        '''
        print("Enter your Zendesk account")
        subdomain = input("Subdomain: ")
        email = input ("Email: ")
        password = input("Password: ")
        return subdomain, email, password
    
    def status_401(self):
        '''
            Function to let the user know that the program can't authenticate them
            Return none
        '''
        print("-" * 41)
        print("|   Couldn't authenticate you. Code 401 |")
        print("| The username or password is incorrect |")
        print("-" * 41)
    
    
    def status_200(self):
        '''
            Function letting user know if they have valid login information
            Return none
        '''
        print("-" * 41)
        print("|           ACCESS GRANTED              |")
        print("-" * 41)

    def status_500 (self):
        '''
            Prompt if the server crass
            Return none
        '''
        print("*" * 15)
        print("Internal Server Error. Code 500 *")
        print("*" * 15)

    def all_tickets_prompt(self):
        '''
            Function letting user know the data from api have been loaded into the program
                They can choose to execute next step
            Return none
        '''
        print("*" * 54)
        print("*    ALL TICKETS LOADED. Choose from options below   *")
        print("*    Press 1 or 'next' to view the next page         *")
        print("*    Press 2 or 'prev' to view the previous page     *")
        print("*    Press 3 or 'home' to return to main page        *")
        print("*    Type 'quit' to exit                             *")
        print("*" * 54)


    def display(self):
        '''
            Display tickets in pretty format
            Return none
        '''
        print(f"Ticket ID   Subject { ' ' * 45} Created At { ' ' * 15} Assigned By { ' ' * 7} Priority { ' ' * 5} Status")
        print("_" * 140)