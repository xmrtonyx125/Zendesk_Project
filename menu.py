class Menu():
    def __init__(self) -> None:
        pass

    def printMenu(self):
        print("Select view options:")
        print(" * Press 1 to view all tickets")
        print(" * Press 2 to view a ticket")
        print(" * Type 'quit' to exit\n")
        

    def exit_Prompt(self):
        print("Thank you for using the viewer.")
        print("Have a good day\n") 
    
    def welcome_Prompt(self):
        print("Welcome to the ticket viewer\n")
        print("Type 'menu' to view option or 'quit' to exit\n")
        