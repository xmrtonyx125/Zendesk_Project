
import requests
from prompt import Menu
from exception import ZendeskExceptions


base_URL = "https://zendeskcodingchallenge2945.zendesk.com/api/v2/tickets.json"


class API():
    def __init__(self) -> None:
        pass


    def get_response_code(self, subdomain, email, password ):
        '''
           Function to get data from api 

        '''
        response = requests.get("https://" + subdomain + ".zendesk.com/api/v2/tickets.json", auth = (email, password))
        
        
        return response
