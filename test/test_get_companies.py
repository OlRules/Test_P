import pytest
# import requests
# from data.urls import base_url
from data.data_files import StatusCompanies
from src.my_requests import MyRequests


from pprint import pprint


# base_url = "https://send-request.me/api/companies"
# status_list = ['ACTIVE', 'CLOSED', 'BANKRUPT']
# status_list = StatusCompanies.status_list

class TestStatusCompanies:
    status_list = StatusCompanies.status_list
    request = MyRequests()

    @pytest.mark.parametrize('status', status_list)
    def test_get_statuses_companies(self, status):
        response = self.request.get(f"/?status={status}&limit=3&offset=0")
        assert response.status_code == 200, f'Status code is not 200, status code is {response.status_code}'

        # print()
        # pprint(response.json())

    @pytest.mark.parametrize("status", status_list)
    def test_get_closed_companies(self, status):
        response = self.request.get(f"""/?status={status}&limit=3&offset=0""")
        print()
        pprint(response.headers)
        assert response.status_code == 200, f'Status code is not 200, status code is {response.status_code}'
        # print(response.headers)

    #
    @pytest.mark.parametrize("status", status_list)
    def test_get_bankrupt_companies(self, status):
        response = self.request.get(f"""/?status={status}&limit=3&offset=0""")
        items_list = response.json()['data']
        for item in range(len(items_list)):
            print(items_list[item]['company_status'])
            assert item['company_status'] == status
        # print(items_list)
        # print(response.json()['data'][0]['company_status'])
        # pprint(response.json())
