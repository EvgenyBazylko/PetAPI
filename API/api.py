import json
import requests
from data import LoginData
import uuid
#import os
#from dotenv import load_dotenv
"""Устанавливаем пакет dotenv"""

#load_dotenv()
"""Импортируем пакет dotenv"""
LD = LoginData()

class Pets:
    """API библиотека для учебного сваггера url: http://34.141.58.52:80000/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'


    """Следующая функция (функция ниже) нужна для получения токена при логине (POST/login)"""
    def login_user(self) -> json:
        data = {
            "email": LD.VALID_EMAIL,
            "password": LD.VALID_PASSWORD
        }
        response = requests.post(self.base_url + 'login', data=json.dumps(data))
        user_token = response.json()["token"]
        user_id = response.json()["id"]
        status_code = response.status_code
        return user_token, user_id, status_code
    """Очередность следующая: user_token - 0-ой эл-т, user_id - 1-ый эл-т, status_code - 2-ой эл-т"""

    """Функция добавления питомца (POST/pet)"""
    def create_pet(self) -> json:
        user_id = self.login_user()[1]
        user_token = self.login_user()[0]
        headers = {'Authorization': f'Bearer {user_token}'}
        data = {
            "name": "Stim",
            "type": "cat",
            "age": 3,
            "gender": "Male",
            "owner_id": user_id,
        }
        response = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = response.json()["id"]
        status_code = response.status_code
        return pet_id, status_code


    """Функция получения списка пользователей (GET/users)"""
    def users_list(self) -> json:
        user_token = self.login_user()[0]
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.get(self.base_url + 'users', headers=headers)
        user_id = response.json()
        status_code = response.status_code
        return user_id, status_code


    """Функция получения информации о питомце (GET/pet/{id})"""
    def get_pet(self) -> json:
        pet_id = self.create_pet()[0]
        response = requests.get(self.base_url + f'pet/{pet_id}')
        pet_body = response.json()['pet']
        comments_body = response.json()['comments']
        status_code = response.status_code
        return pet_body, comments_body, status_code


    """Функция добавления лайка питомцу (PUT/pet/{id}/like)"""
    def add_like(self) -> json:
        pet_id = self.create_pet()[0]
        user_token = self.login_user()[0]
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status_code = response.status_code
        return status_code


    """Функция добавления комментария питомцу (PUT/pet/{id}/comment)"""
    def add_comment(self) -> json:
        pet_id = self.create_pet()[0]
        user_token = self.login_user()[0]
        user_id = self.login_user()[1]
        headers = {'Authorization': f'Bearer {user_token}'}
        data = {
            "pet_id": pet_id,
            "message": "Какой у вас красивый питомец!",
            "user_id": user_id,
            "user_name": LD.VALID_EMAIL
        }
        response = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        comment_id = response.json()['id']
        status_code = response.status_code
        return comment_id, status_code


    """Функция получения списка указанных питомцев (POST/pets)"""
    def pets_list(self) -> json:
        user_token = self.login_user()[0]
        user_id = self.login_user()[1]
        headers = {'Authorization': f'Bearer {user_token}'}
        data = {
            "type": "cat",
            "petName": "Stim",
            "user_id": user_id
        }
        response = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        list_body = response.json()['list']
        total_body = response.json()['total']
        status_code = response.status_code
        return list_body, total_body, status_code


    """Функция обновления данных о питомце (PATCH/pet)"""
    def update_pet(self) -> json:
        user_token = self.login_user()[0]
        user_id = self.login_user()[1]
        pet_id = self.create_pet()[0]
        headers = {'Authorization': f'Bearer {user_token}'}
        data = {
            "id": pet_id,
            "name": "Grey",
            "type": "cat",
            "age": 5,
            "gender": "Male",
            "owner_id": user_id,
            "owner_name": LD.VALID_EMAIL,
        }
        response = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id_body = response.json()['id']
        status_code = response.status_code
        return pet_id_body, status_code


    """Функция добавления картинки питомцу (POST/pet/{id}/image)"""
    def upload_image(self) -> json:
        pet_id = self.create_pet()[0]
        user_token = self.login_user()[0]
        headers = {'Authorization': f'Bearer {user_token}'}
        files = {'pic': ('dog.jpg', open('C:\\Users\\Evgenij\\PycharmProjects\\PetAPI\\tests\\Photo\\dog.jpg', 'rb'), 'image/jpg')}
        response = requests.post(self.base_url + f'pet/{pet_id}/image', files=files, headers=headers)
        link_body = response.json()['link']
        status_code = response.status_code
        return link_body, status_code


    """Функция удаления питомца (DELETE/pet/{id})"""
    def delete_pet(self) -> json:
        pet_id = self.create_pet()[0]
        user_token = self.login_user()[0]
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status_code = response.status_code
        return status_code











#Pets().login_user()
#Pets().create_pet()
#Pets().users_list()
#Pets().get_pet()
#Pets().add_like()
#Pets().add_comment()
#Pets().pets_list()
#Pets().update_pet()
#Pets().upload_image()
#Pets().delete_pet()