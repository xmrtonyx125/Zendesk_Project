import unittest
from API_call import API
from prompt import Menu

api = API()
menu = Menu()

class Test(unittest.TestCase):

    def test_Login_fail(self):
        self.assertTrue(api.get_response_code("fakesubdomain","real@gmail.com", "truepasword").status_code == 200 , "Couldn't authenticate you. Code 401")


    def test_Login_success(self):
        self.assertTrue(api.get_response_code("zendeskcodingchallenge2945","phanthanhan2107@gmail.com", "Xmrtonyxdjrun90@@").status_code == 200 , "Fail to Login")





if __name__ == '__main__':
    unittest.main()