from prompt import Menu
from API_call import API
from datetime import datetime

subdomain = "zendeskcodingchallenge2945"
email = "phanthanhan2107@gmail.com"
password = "Xmrtonyxdjrun90@@"

menu = Menu()
api = API()
#subdomain, email, password = menu.login_Prompt() 

response = api.get_response_code(subdomain, email, password)
subject = ""
created_at = "" 
assignee_id = "" 
priority = ""
status = ""
user_input = ""
prompt_input = ""
option_2_input = ""
count = 0
i= 0

if (response.status_code == 401):
    menu.status_401()

elif (response.status_code == 500):
    menu.status_500()

elif (response.status_code == 200):
    menu.status_200()
    data = response.json()
    tickets = data['tickets']
    subject =  [element['subject'] for element in tickets]
    created_at = [element['created_at'] for element in tickets]
    assignee_id = [element['assignee_id'] for element in tickets]
    priority = [element['priority'] for element in tickets]
    status = [element['status'] for element in tickets]

    number_of_subject = len(subject)
    number_of_created_at = len (created_at)
    for y in range(number_of_subject):
        created_at[y] = str(datetime.strptime(created_at[y], '%Y-%m-%dT%H:%M:%SZ'))
        if (priority[y] == None):
            priority[y] = 'None'

    while (user_input != 'menu' or user_input ==  'quit' or user_input == 'exit'):
        user_input = ""
        user_input = menu.welcome_Prompt()
        
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
                                    print  (f"{i+1 : <10}  {subject[i] : <52} {created_at[i] : <25}  {assignee_id[i] : <20} {priority[i] : <15} {status[i] : <15}");
                            
                            else:
                                print("You hit the end of the ticket's list. Press 2 to return to the previous page")
                                i = number_of_subject 
                                count = number_of_subject  
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
                                
                        print('\n')    
                    
                    elif menu_input == '2':
                        option_2_input = ""
                        ticket_number = input("Enter a ticket number: ")
                        ticket_number = int(ticket_number)
                        increase_tick_num = ticket_number-1
                        if (ticket_number < 0 or ticket_number > number_of_subject):
                            print(f"Out of range. Choose from 1 to {number_of_subject}")
                            break
                        menu.display()
                        print (f"{ticket_number : <10}  {subject[increase_tick_num] : <52}  {created_at[increase_tick_num] : <25}  {assignee_id[increase_tick_num] : <20}")
                        print('\n')
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
    print("| Login failed. Error code: ", response.status_code, "|")
    print("-" * 34)
