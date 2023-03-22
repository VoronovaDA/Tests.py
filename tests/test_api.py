import pytest
import requests

token = (['...'])


@pytest.mark.parametrize('token', token)
class TestApi:

    def test_api_create_folder(self, token):
        response = requests.put('https://cloud-api.yandex.net:443/v1/disk/resources',
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"OAuth {token}"},
                                params={'path': '/Тест папка'})
        assert response.status_code == 201 or response.status_code == 409

    def test_api_check_folder(self, token):
        response = requests.get('https://cloud-api.yandex.net:443/v1/disk/resources',
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"OAuth {token}"},
                                params={'path': '/Тест папка'})
        assert response.status_code == 200
