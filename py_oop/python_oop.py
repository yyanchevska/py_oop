"""
Description: Create TestRail client for generating Test Suites

Features:
- TestSuite should be created with (username list(First Name/Last Name), user_email, user_password)
- Show in test cases all user data except password (password should be shown as '********')
- Create test suite for login/registration/article create flow
- Please use the same steps in common methods
- Validate valid user email and profile

Testing:
- Run all your testsuite using calling methods for suite_object
"""


class TestRunBuilder:
    url = 'https://qamay2021.testrail.io'
    #firstname = test123
    #lastname = test123
    #user_email = test123@gmail.com
    #user_password = test123

    def __init__(self, firstname, lastname, user_email, user_password):
        print ('TestTrail Lauched')
        self.firstname = firstname
        self.lastname = lastname
        self.user_email = user_email
        self.user_password = user_password

    def login_base_flow(self):
        print('Open "/login" page')
        print(f'Fill user_email field as {self.user_email}')
        print('Check user_mail field validation, field can\'t be blank')
        print(f'Fill user_password field as {self.user_password}')
        print('Check user_password field validation, field can\'t be blank')
        print('Check that user_password is shown as "********"')
        print('Click [Login] button')

    def login_test_suit(self):
        print('--------------------------------------')
        self.login_base_flow()
        print('Check redirect into "/home" page')

    def registration_test_suit(self):
        print('--------------------------------------')
        print('Open /registration page')
        print(f'Fill firstname field as {self.firstname}')
        print(f'Fill lastname field as {self.lastname}')
        print(f'Fill user_email field as {self.user_email}')
        print('Check user_mail field validation, field can\'t be blank')
        print(f'Fill user_password field as {self.user_password}')
        print('Check that user_password is shown as "********"')
        print('Check user_password field validation, field can\'t be blank')
        print('Click [Registration] button')
        print('Check redirect into "/home" page')

    def create_artile(self):
        print('--------------------------------------')
        self.login_base_flow()
        print('Check redirect into "/home" page')
        print('Click on [Create article] button')
        print('Fill all field as a test1 data')
        print('Click on [Publish] button')
        print('Check all filled fields in Article preview screen')

    def smoke_test_run(self):
        print('--------------------------------------')
        print('You are running smoke flow')
        self.login_test_suit()

    def regression_test_run(self):
        print('--------------------------------------')
        print('You are running regression flow')
        self.login_test_suit()
        self.registration_test_suit()
        self.create_artile()

test_run_smoke = TestRunBuilder('test', '123', 'test123@gmail.com', 'test123')
test_run_smoke.registration_test_suit()
test_run_smoke.login_test_suit()
test_run_smoke.create_artile()

#test_run_sanity = TestRunBuilder(username, user_email, user_password)
#test_run_regression = TestRunBuilder(username, user_email, user_password)

