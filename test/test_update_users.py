from src.my_requests import MyRequests
from data.status_code import StatusCode
from src.assertions import Assertion

class TestCreateUsers:
    assertion = Assertion()
    status_code = StatusCode()
    body = {
    'first_name': 'David',
    'last_name': 'Davidov',
    'company_id': 2
    }


    def test_update_user(self):
        response = MyRequests.put('/users/24190', self.body)
        print(response.json())
        assert response.json()['first_name'] != 'Nicholas', "First name was not update"
        assert response.json()['last_name'] != 'Nguyen', "Last name was not update"
        self.assertion.assert_status_code(response, self.status_code.OK)