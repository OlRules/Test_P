from src.my_requests import MyRequests


class TestCreateUsers:
    body = {
    'first_name': 'Denis',
    'last_name': 'Denis2',
    'company_id': 1
    }

    def test_create_user(self):
        response = MyRequests.post('/users/', self.body)
        assert response.json()['first_name']  == self.body.get('first_name'), "First name was not created"
        assert response.json()['last_name'] == self.body.get('last_name'), "last name was not created"
        print(response.json())
    def test_get_status_code_201(self):
        response = MyRequests.post('/users/', self.body)
        assert response.status_code  == 201, f"Status code not 201, status code is {response.status_code}"


