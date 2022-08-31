import requests
from api_testing.pet_models.pet import Pet


class PetApi:
    def __init__(self, url=None):
        if url is None:
            self.url = "https://petstore3.swagger.io/api/v3"
        else:
            self.url = url
        self.headers = {'accept': 'application/json'}
        self.session = requests.session()
        self.session.headers.update(self.headers)

    def put_pet(self, pet):
        pet_data = pet.to_json()
        response = self.session.put(url=f"{self.url}/pet", data=pet_data)
        return response

    def post_new_pet(self, pet):
        pet_data = pet.to_json()
        response = self.session.post(url=f"{self.url}/pet", data=pet_data)
        return response

    def post_pet_by_id_and_update(self, pet_id: int, name: str, status: str):
        response = self.session.post(url=f"{self.url}/pet/{pet_id}?name={name}&status={status}")
        return response

    def get_pet_by_id(self, pet_id: int):
        response = self.session.get(url=f"{self.url}/pet/{pet_id}")
        return response

    def get_pets_by_status(self, status) -> [Pet]:
        response = self.session.get(url=f"{self.url}/pet/findByStatus?status={status}")
        return response

    def get_pet_by_tags(self, tags):
        tagsString = f'tags={tags[0]}'
        if not isinstance(tags, list):
            raise TypeError("tags must be a list of strings!")
        if len(tags) > 1:
            for tag in range(1, len(tags)):
                if not isinstance(tags[tag], str):
                    raise TypeError("one or more of the tags is not a string!")
                tagsString += f'&tags={tags[tag]}'
        response = self.session.get(url=f"{self.url}/pet/findByTags?{tagsString}")
        return response

    def upload_image_by_id(self, pet_id: int, files):
        response = self.session.post(url=f"{self.url}/pet/{pet_id}/uploadImage", files=files)
        return response

    def delete_pet_by_id(self, pet_id: int):
        response = self.session.delete(url=f"{self.url}/pet/{pet_id}")
        return response