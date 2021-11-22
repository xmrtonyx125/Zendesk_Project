
import requests
from prompt import Menu


base_URL = "https://zendeskcodingchallenge2945.zendesk.com/api/v2/tickets.json"

subdomain = "zendeskcodingchallenge2945"
email = "phanthanhan2107@gmail.com"
password = "Xmrtonyxdjrun90@@"

class API():
    def __init__(self) -> None:
        pass


    def get_response_code(self):
        menu = Menu()
        #subdomain, email, password = menu.login_Prompt() 
        subject = "" 
        created_at = "" 
        assignee_id = ""
        response = requests.get("https://" + subdomain + ".zendesk.com/api/v2/tickets.json", auth = (email, password))
        if (response.status_code == 200):
            data = response.json()
            print(response.status_code)
            tickets = data['tickets']
            subject =  [element['subject'] for element in tickets]
            created_at = [element['created_at'] for element in tickets]
            assignee_id = [element['assignee_id'] for element in tickets]
        return response.status_code, subject, created_at, assignee_id
