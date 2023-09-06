from data import LoginData
from API.api import Pets

pet = Pets()
LD = LoginData()


"""Тест на регистрацию пользователя (POST/login)"""
def test_login_user():
    status_code = pet.login_user()[2]
    user_token = pet.login_user()[0]
    assert status_code == 200
    assert user_token


"""Тест на добавление питомца (POST/pet)"""
def test_create_pet():
    res = pet.create_pet()
    status_code = res[1]
    pet_id = res[0]
    assert status_code == 200
    assert pet_id


"""Тест на получение списка пользователей (GET/users)"""
def test_users_list():
    user_id = pet.users_list()[0]
    status_code = pet.users_list()[1]
    assert user_id
    assert status_code == 200


"""Тест на получение информации о питомце (GET/pet/{id})"""
def test_get_pet():
    res = pet.get_pet()
    pet_body = res[0]
    comments_body = res[1]
    status_code = res[2]
    assert pet_body
    assert type(comments_body) == list
    assert status_code == 200


"""Тест на добавление лайка питомцу (PUT/pet/{id}/like)"""
def test_add_like():
    status_code = pet.add_like()
    assert status_code == 200


"""Тест на добавление комментария питомцу (PUT/pet/{id}/comment)"""
def test_add_comment():
    res = pet.add_comment()
    comment_id = res[0]
    status_code = res[1]
    assert comment_id
    assert status_code == 200


"""Тест на получение списка указанных питомцев (POST/pets)"""
def test_pets_list():
    list_body = pet.pets_list()[0]
    total_body = pet.pets_list()[1]
    status_code = pet.pets_list()[2]
    assert list_body
    assert total_body
    assert status_code == 200


"""Тест на обновление данных о питомце (PATCH/pet)"""
def test_update_pet():
    res = pet.update_pet()
    pet_id_body = res[0]
    status_code = res[1]
    assert pet_id_body
    assert status_code == 200


"""Тест на добавление картинки питомцу (POST/pet/{id}/image)"""
def test_upload_image():
    res = pet.upload_image()
    link_body = res[0]
    status_code = res[1]
    assert link_body
    assert status_code == 200


"""Тест на удаление питомца (DELETE/pet/{id})"""
def test_delete_pet():
    status_code = pet.delete_pet()
    assert status_code == 200