
import requests

class API():
    def __init__(self) -> None:
        pass


    def get_response_code(self, subdomain, email, password ):
        '''
            Function to get data from api 

            Arguments:
                subdomain {string} -- enter by user
                email {string}  -- enter by user
                password {string}  -- enter by user

            Return:
                status_code {int} -- code return by api (200 == success, 401 == authentical error, 404 == not found domain)
                subject, created_at, assignee_id, priority, status {list of string} -- fetched data from api 

        '''
        subject =  ""
        created_at = ""
        assignee_id = ""
        priority = ""
        status = ""
        requester_id = "" 
        submitter_id = ""
        description = ""
        response = requests.get("https://" + subdomain + ".zendesk.com/api/v2/tickets.json", auth = (email, password))
        if (response.status_code == 200):
            data = response.json()
            tickets = data['tickets']
            subject =  [element['subject'] for element in tickets]
            created_at = [element['created_at'] for element in tickets]
            assignee_id = [element['assignee_id'] for element in tickets]
            priority = [element['priority'] for element in tickets]
            status = [element['status'] for element in tickets]
            requester_id = [element['requester_id'] for element in tickets]
            submitter_id = [element['submitter_id'] for element in tickets]
            description = [element['description'] for element in tickets]

        return (response.status_code, subject, 
                created_at, assignee_id, priority, status,
                requester_id, submitter_id, description)

    def check_user_input(self, input):
        '''
            Check if the input of the user IS a number
            return True if it is a number
            return False if it is not a number (float, string, or number+string)
        '''
        if input.isdigit():
            return True;
        return False