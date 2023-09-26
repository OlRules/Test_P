import requests
from requests import Response




class Assertion:

    def assert_status_code(self, response: Response, expected_status_code: int):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, f"Unexpected status code. Expected {expected_status_code}, Actual: {actual_status_code}"