import requests


class UserApi:
    def __init__(self, url=None):
        if url is None:
            self._url = "https://petstore3.swagger.io/api/v3/user"
        else:
            self._url = url
        self._headers = {"accept": "application/json"}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def post_user(self, user):
        user_data = user.to_json()
        response = self._session.post(url=f"{self._url}", data=user_data)
        return response

    def post_users_list(self, users):
        response = self._session.post(url=f"{self._url}/createWithList", data=users)
        return response

    def get_login(self, user_name, password):
        response = self._session.get(url=f"{self._url}/login?username={user_name}&password={password}")
        return response

    def get_logout(self):
        response = self._session.get(url=f"{self._url}/logout")
        return response

    def get_username(self, user_name: str):
        response = self._session.get(url=f"{self._url}/{user_name}")
        return response

    def put_username(self, user):
        response = self._session.put(url=f"{self._url}/{user}", data=user)
        return response

    def delete_username(self, user_name: str):
        response = self._session.delete(url=f"{self._url}/{user_name}")
        return response
