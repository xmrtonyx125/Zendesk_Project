from prompt import Menu
menu = Menu()


class Page():
    def list_25_ticket(i , count, number_of_subject)
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