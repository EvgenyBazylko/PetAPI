from API.e2e import e2e

e = e2e()

def test_life_user():
    res = e.life_user()
    """Регистрация пользователя (POST/register)"""
    user_token = res[0]
    user_email = res[1]
    user_id = res[2]
    """Вход в уже созданный аккаунт пользователя (POST/login)"""
    user_token_login = res[3]
    user_id_login = res[4]
    status_code_login = res[5]
    """Создание питомца (POST/pet)"""
    pet_id = res[6]
    status_code_create = res[7]
    """Добавление картинки питомцу (POST/pet/{id}/image)"""
    link_body = res[8]
    status_code_image = res[9]
    """Добавление лайка питомцу (PUT/pet/{id}/like)"""
    status_code_like = res[10]
    """Добавление комментария питомцу (PUT/pet/{id}/comment)"""
    comment_id = res[11]
    status_code_comment = res[12]
    """Обновление данных о питомце (PATCH/pet)"""
    pet_id_update = res[13]
    status_code_update = res[14]
    """Удаление питомца (DELETE/pet/{id})"""
    status_code_del_pet = res[15]
    """Удаление пользователя (DELETE/users/{id})"""
    status_code_del_user = res[16]
    assert user_token
    assert user_email
    assert user_id
    assert user_token_login
    assert user_id_login
    assert status_code_login == 200
    assert pet_id
    assert status_code_create == 200
    assert link_body
    assert status_code_image == 200
    assert status_code_like == 200
    assert comment_id
    assert status_code_comment == 200
    assert pet_id_update
    assert status_code_update == 200
    assert status_code_del_pet == 200
    assert status_code_del_user == 200