
import requests

base_URL = "https://zendeskcodingchallenge2945.zendesk.com/api/v2/tickets.json"


class API():
    def __init__(self) -> None:
        pass


    def get_Data(self):
        response = requests.get(base_URL)
        print("status code from api: " ,response.status_code, "\n")

