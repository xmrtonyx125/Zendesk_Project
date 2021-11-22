from prompt import Menu
from API_call import API


menu = Menu()
api = API()

return_api_code, subject, created_at = api.get_response_code()

number_of_subject = len(subject)
number_of_created_at = len (created_at)
 
count = 0
i= 0
prompt_input = ""
if (return_api_code == 401):
    menu.status_401()

elif (return_api_code == 500):
    menu.status_500()

elif (return_api_code == 200):
    menu.status_200()


    menu.welcome_Prompt()
    user_input  = input ("\nYour input: ") #type menu or quit
    print("\n")


    if user_input == 'menu':
        
        menu.printMenu()
        menu_input = input ("Your input: ") # choose from 1,2, or quit
        while (menu_input != 'quit') and (menu_input != 'exit'): # Loop until user type quit or exit

            while (prompt_input != 'home' and prompt_input != '3'):
                if menu_input == '1':
                    menu.all_tickets_prompt()
                    prompt_input = input("Your input: ")

                    if (prompt_input == '1'):
                        count += 25
                        if (count >= 0 and count <= number_of_subject):
                            print("count = ", count)
                            for i in range (i, count):
                                #print("i = ", i, "count = ", count)
                                print (f"Ticket ID: {i+1} with subject: '{subject[i]}'")
                        
                        else:
                            print("last page")
                            i = number_of_subject - 1
                            count = number_of_subject - 1 

                    elif (prompt_input == '2'):
                        count -= 25
                        i = count - 24
                        if (count <= 0):
                            count = 0
                            i = 0
                            print("first page")
                            
                        elif (count >= 0 and count <= number_of_subject):
                            print("count = ", count)  
                            for i in range (i, count):
                                #print("i = ", i, "count = ", count)
                                print (f"Ticket ID: {i+1} with subject: '{subject[i]}'")


                
                elif menu_input == '2':
                    menu.a_ticket_prompt()
                    prompt_input = input("Your input: ")
                    print("\n")
                     



                

                
                    
            
            menu.printMenu()
            menu_input = input ("Your input: ")
            prompt_input = "" # reset to enter the second loop
                


        menu.exit_Prompt() # Good-bye message


    elif user_input ==  'quit' or 'exit': # exiting 
        menu.exit_Prompt()  # Good-bye message

else:
    print("Error code ", return_api_code)