import unittest
from API_call import API
from prompt import Menu

api = API()
menu = Menu()

class Test(unittest.TestCase):

    def test_Login_domain_fail(self):
        '''
            Function to test if an invalid domain was given
            
            return_api_code IS the return code from the Internet
                404 code if the program can't find the domain
            If not return 404 code, the domain is valid
        '''
        return_api_code = api.get_response_code("fakesubdomain","phanthanhan2107@gmail.com", "Xmrtonyxdjrun90@@")[0]
        self.assertTrue(return_api_code == 404 , "Login Successfully")

    def test_Login_email_fail(self):
        '''
            Function to test if an invalid email and password were given

            return 401 code if can't authenticate ther user
                If not return 401 code, the email is valid
        '''
        return_api_code = api.get_response_code("zendeskcodingchallenge2945","fake@gmail.com", "TotallyReal")[0]
        self.assertTrue(return_api_code == 401 , "Login Successfully") 


    def test_Login_success(self):
        '''
            Function to test with real login information
            return 200 if the program can authenicate the user
                else print the messeage as below
        '''
        return_api_code = api.get_response_code("zendeskcodingchallenge2945","phanthanhan2107@gmail.com", "Xmrtonyxdjrun90@@")[0]
        self.assertTrue(return_api_code == 200 , "Couldn't authenticate you")


if __name__ == '__main__':
    unittest.main()