import json
import requests
from data import LoginData
import uuid

class e2e:
    """API библиотека для учебного сваггера url: http://34.141.58.52:80000/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def life_user(self) -> json:
        """Регистрация пользователя (POST/register)"""
        e = uuid.uuid4().hex
        data_reg = {
            "email": f"{e}@gmail.com",
            "password": "1234",
            "confirm_password": "1234"
        }
        response = requests.post(self.base_url + 'register', data=json.dumps(data_reg))
        user_token = response.json()["token"]
        user_email = response.json()['email']
        user_id = response.json()["id"]

        """Вход в уже созданный аккаунт пользователя (POST/login)"""
        data_log = {
            "email": user_email,
            "password": "1234"
        }
        response = requests.post(self.base_url + 'login', data=json.dumps(data_log))
        user_token_login = response.json()["token"]
        user_id_login = response.json()["id"]
        status_code_login = response.status_code

        """Создание питомца (POST/pet)"""
        headers = {'Authorization': f'Bearer {user_token}'}
        data_pet = {
            "name": "Stim",
            "type": "cat",
            "age": 3,
            "gender": "Male",
            "owner_id": user_id,
        }
        response = requests.post(self.base_url + 'pet', data=json.dumps(data_pet), headers=headers)
        pet_id = response.json()["id"]
        status_code_create = response.status_code

        """Добавление картинки питомцу (POST/pet/{id}/image)"""
        headers = {'Authorization': f'Bearer {user_token}'}
        files = {'pic': ('dog.jpg', open('C:\\Users\\Evgenij\\PycharmProjects\\PetAPI\\tests\\Photo\\dog.jpg', 'rb'), 'image/jpg')}
        response = requests.post(self.base_url + f'pet/{pet_id}/image', files=files, headers=headers)
        link_body = response.json()['link']
        status_code_image = response.status_code

        """Добавление лайка питомцу (PUT/pet/{id}/like)"""
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status_code_like = response.status_code

        """Добавление комментария питомцу (PUT/pet/{id}/comment)"""
        headers = {'Authorization': f'Bearer {user_token}'}
        data_com = {
            "pet_id": pet_id,
            "message": "Какой у вас красивый питомец!",
            "user_id": user_id,
            "user_name": user_email
        }
        response = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data_com), headers=headers)
        comment_id = response.json()['id']
        status_code_comment = response.status_code

        """Обновление данных о питомце (PATCH/pet)"""
        headers = {'Authorization': f'Bearer {user_token}'}
        data_upd = {
            "id": pet_id,
            "name": "Grey",
            "type": "cat",
            "age": 5,
            "gender": "Male",
            "owner_id": user_id,
            "owner_name": user_email
        }
        response = requests.patch(self.base_url + 'pet', data=json.dumps(data_upd), headers=headers)
        pet_id_update = response.json()['id']
        status_code_update = response.status_code

        """Удаление питомца (DELETE/pet/{id})"""
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status_code_del_pet = response.status_code

        """Удаление пользователя (DELETE/users/{id})"""
        headers = {'Authorization': f'Bearer {user_token}'}
        params = {'id': user_id}
        response = requests.delete(self.base_url + f'users/{user_id}', headers=headers, params=params)
        status_code_del_user = response.status_code
        return user_token, user_email, user_id, user_token_login, user_id_login, status_code_login, pet_id, status_code_create, link_body, status_code_image, status_code_like, comment_id, status_code_comment, pet_id_update, status_code_update, status_code_del_pet, status_code_del_user

#e2e().life_user()