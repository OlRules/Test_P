from src.my_requests import MyRequests

class TestDeleteUsers:

    def test_delete_users(self):
        response = MyRequests.delete('/users/22448')
        print(response.text)
        assert response.status_code == 202, f"Status code not 202, status code is {response.status_code}"

    def test_delete_users_has_text_null(self):
        response = MyRequests.delete('/users/22449')
        print(response.text)
        assert response.text == "null", "Wrong text"


    def test_delete_deleted_users_has_status_code_404(self):
        response = MyRequests.delete('/users/22446')
        print(response.json())
        assert response.status_code == 404, f"Status code not 404, status code is {response.status_code}"

    def test_delete_deleted_users_has_text(self):
        response = MyRequests.delete('/users/22446')
        assert response.json()['detail']['reason'] == "User with requested id: 22446 is absent", "Wrong text"
