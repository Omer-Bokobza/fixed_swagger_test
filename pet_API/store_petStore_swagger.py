import requests
from api_testing.pet_models.pet import Pet


class OrderApi:
    def __init__(self, url=None):
        if url is None:
            self._url = "https://petstore3.swagger.io/api/v3/store"
        else:
            self._url = url
        self._headers = {"accept": "application/json"}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def get_store_inventory(self):
        response = self._session.get(url=f"{self._url}/inventory")
        return response

    def post_order(self, order):
        order_data = order.to_json()
        response = self._session.post(url=f"{self._url}/order", data=order_data)
        return response

    def get_order(self, id: int) -> [Pet]:
        response = self._session.get(url=f"{self._url}/order/{id}")
        return response

    def delete_order(self, id: int) -> [Pet]:
        response = self._session.delete(url=f"{self._url}/order/{id}")
        return response