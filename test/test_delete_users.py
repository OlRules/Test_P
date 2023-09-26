from src.my_requests import MyRequests
from src.assertions import Assertion
from data.status_code import StatusCode


class TestDeleteUsers:
    assertions = Assertion()
    status_code = StatusCode()

    def test_delete_users(self):
        response = MyRequests.delete('/users/24195')
        self.assertions.assert_status_code(response,self.status_code.ACTUAL)

    def test_delete_users_has_text_null(self):
        response = MyRequests.delete('/users/22449')
        actual_text = response.text
        self.assertions.assert_text(actual_text, "null")


    def test_delete_deleted_users_has_status_code_404(self):
        response = MyRequests.delete('/users/22446')
        print(response.json())
        self.assertions.assert_status_code(response,self.status_code.NOT_FOUND)

    def test_delete_deleted_users_has_text(self):
        response = MyRequests.delete('/users/22446')
        actual_text = response.json()['detail']['reason']
        self.assertions.assert_text(actual_text,"User with requested id: 22446 is absent")
