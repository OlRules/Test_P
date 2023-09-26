from src.my_requests import MyRequests
from generator.generator import generated_person
from src.assertions import Assertion
from data.status_code import StatusCode

class TestCreateUsers:
    assertions = Assertion()
    status_code = StatusCode()

    def get_body(self,first_name, last_name, company_id):
        body = {
            'first_name': first_name,
            'last_name': last_name,
            'company_id': company_id
        }
        return body
    def test_create_user(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        company_id = person_info.company_id
        response = MyRequests.post('/users/', self.get_body(first_name, last_name, company_id))
        body = response.json()
        print(body)
        assert body['first_name']  == first_name, "First name was not created"
        assert body['last_name'] == last_name, "last name was not created"

    def test_get_status_code_201(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        company_id = person_info.company_id
        response = MyRequests.post('/users/', self.get_body(first_name, last_name, company_id))
        self.assertions.assert_status_code(response, self.status_code.CREATE)
        # assert response.status_code  == 201, f"Status code not 201, status code is {response.status_code}"


