from prompt import Menu
from API_call import API
from datetime import datetime


menu = Menu()
api = API()
subdomain, email, password = menu.login_Prompt() 

if subdomain == "" or email == "" or password == "":
    print(f"Subdomain, email or password need to be fill\n")
    exit(1)

(return_api_code, subject, created_at, assignee_id, 
priority, status, requester_id, submitter_id, description) = api.get_response_code(subdomain, email, password)

number_of_subject = len(subject)
number_of_created_at = len (created_at)
for y in range(number_of_subject):
    created_at[y] = str(datetime.strptime(created_at[y], '%Y-%m-%dT%H:%M:%SZ'))
    if (priority[y] == None):
        priority[y] = 'None'
count = 0
i= 0
user_input = ""
prompt_input = ""
option_2_input = ""
if (return_api_code == 401):
    menu.status_401()

elif (return_api_code == 500):
    menu.status_500()

elif (return_api_code == 200):
    menu.status_200()

    while (user_input != 'menu' or user_input ==  'quit' or user_input == 'exit'):
        user_input = ""
        menu.welcome_Prompt()
        user_input  = input ("Your input: ") #type menu or quit
        print("\n")
        if user_input == 'menu':
            
            menu.printMenu()
            menu_input = input ("Your input: ") # choose from 1,2, or quit
            print("\n")
            while (menu_input != 'quit') and (menu_input != 'exit'): # Loop until user type quit or exit
                while (prompt_input != 'home' and prompt_input != '3'):
                    if menu_input == '1':
                        
                        menu.all_tickets_prompt()
                        prompt_input = input("Your input: ")
                        print("\n")    
                        if (prompt_input == '1'):
                            menu.display()
                            count += 25
                            if (count >= 0 and count <= number_of_subject):
                                for i in range (i, count):
                                    #print("i = ", i, "count = ", count)
                                    print  (f"{i+1 : <10}  {subject[i] : <52} {created_at[i] : <25}  {assignee_id[i] : <20} {priority[i] : <15} {status[i] : <15}")
                            
                            else:
                                print("You hit the end of the ticket's list. Press 2 to return to the previous page")
                                i = number_of_subject +25
                                count = number_of_subject+25  
                            i += 1
                        elif (prompt_input == '2'):
                            count -= 25
                            i = count - 25
                            menu.display()
                            if (count <= 0):
                                count = 0
                                i = 0
                                print("This is the first page of the ticket's list. Press 1 to go to the next page")
                                
                            elif (count >= 0 and count <= number_of_subject):
                                for i in range (i, count):
                                    #print("i = ", i, "count = ", count)
                                    print (f"{i+1 : <10}  {subject[i] : <52} {created_at[i] : <25}  {assignee_id[i] : <20} {priority[i] : <15} {status[i] : <12}")
                            

                        elif (prompt_input == 'quit' or prompt_input == 'exit'):
                                menu.exit_Prompt()  # Good-bye message
                                exit(1)

                        elif prompt_input == '3': continue
                        
                        else:
                            menu.error_option()
                                
                        print('\n')    
                    
                    elif menu_input == '2':
                        option_2_input = ""
                        ticket_number = input("Enter a ticket number: ")
                        if (api.check_user_input(ticket_number) == True):
                            ticket_number = int(ticket_number) #  cast to type int for position of the list
                        else:      # if it not a digit, break the loop
                            print(f"Input {ticket_number} is not valid. It must be an integer\n")
                            break
                        increase_tick_num = ticket_number-1
                        if (ticket_number < 0 or ticket_number > number_of_subject):
                            print("----")
                            print(f"Out of range. Choose from 1 to {number_of_subject}")
                            print("----")
                            continue
                        
                        print (f" Ticket ID: {ticket_number} with subject '{subject[increase_tick_num]}' created at {created_at[increase_tick_num]} by customer {requester_id[increase_tick_num]}.")
                        print (f" The ticket has been assign to {assignee_id[increase_tick_num]}. ")
                        print (f"????")
                        print (f" Ticket description: '{description[increase_tick_num]}' ")
                        print (f"????")
                        print ('\n')
                        #break
                        yes_no = menu.search_again()
                        if (yes_no == 'n' or yes_no == 'no'):
                            break
                        elif (yes_no == 'y' or yes_no == 'yes'):
                            continue
                        else:
                            menu.error_option()
                    
                    
                    else:
                        menu.error_option()
                        break
                menu.printMenu()
                menu_input = input ("Your input: ")
                print("\n")
                prompt_input = "" # reset to enter the second loop
        
            menu.exit_Prompt() # Good-bye message

        elif user_input ==  'quit' or user_input == 'exit': # exiting 
            menu.exit_Prompt()  # Good-bye message
            exit(1)
        else:
            print(f"Choose again")
        

else:
    print("-" * 34)
    print("| Login failed. Error code: ", return_api_code, "|")
    print("-" * 34)
