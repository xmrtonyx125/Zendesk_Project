import unittest
from API_call import API
from prompt import Menu

api = API()
menu = Menu()

class Test(unittest.TestCase):

    def test_Login_domain_fail(self):
        return_api_code = api.get_response_code("fakesubdomain","phanthanhan2107@gmail.com", "Xmrtonyxdjrun90@@")[0]
        self.assertTrue(return_api_code == 404 , "Login Successfully")

    def test_Login_email_fail(self):
        return_api_code = api.get_response_code("zendeskcodingchallenge2945","fake@gmail.com", "Xmrtonyxdjrun90@@")[0]
        self.assertTrue(return_api_code == 401 , "Login Successfully") 


    def test_Login_success(self):
        return_api_code = api.get_response_code("zendeskcodingchallenge2945","phanthanhan2107@gmail.com", "Xmrtonyxdjrun90@@")[0]
        self.assertTrue(return_api_code == 200 , "Couldn't authenticate you")





if __name__ == '__main__':
    unittest.main()