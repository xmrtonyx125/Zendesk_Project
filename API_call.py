
import requests
from menu import Menu


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
        return response.status_code

