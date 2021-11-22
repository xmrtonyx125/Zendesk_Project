
import requests
from prompt import Menu


base_URL = "https://zendeskcodingchallenge2945.zendesk.com/api/v2/tickets.json"

email = "phanthanhan2107@gmail.com"
password = "Xmrtonyxdjrun90@@"

class API():
    def __init__(self) -> None:
        pass


    def get_response_code(self):
        menu = Menu()
        #email, password = menu.login_Prompt() 

        response = requests.get(base_URL, auth = (email, password))
        data = response.json()

        tickets = data['tickets']
        subject =  [element['subject'] for element in tickets]
        created_at = [element['created_at'] for element in tickets]

        return response.status_code, subject, created_at
