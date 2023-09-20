from src.my_requests import MyRequests

class TestCreateUsers:
    body = {
    'first_name': 'David',
    'last_name': 'Davidov',
    'company_id': 2
    }


    def test_update_user(self):
        response = MyRequests.put('/users/22446', self.body)
        print(response.json())
        assert response.json()['first_name'] != 'Denis', "First name was not update"
        assert response.json()['last_name'] != 'Denis2', "Last name was not update"
        assert response.status_code == 200, f"Status code not 200, status code is {response.status_code}"