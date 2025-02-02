import pytest
import requests
from base.create_courier import register_new_courier_and_return_login_password
from faker import Faker


@pytest.fixture
def courier():
    login, password, first_name = register_new_courier_and_return_login_password()
    login_response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data={"login": login, "password": password})
    assert login_response.status_code == 200
    new_courier_id = login_response.json()['id']
    yield {
        'id': new_courier_id,
        'login': login,
        'password': password,
        'firstName': first_name
    }
    delete_response = requests.delete(f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{new_courier_id}")
    assert delete_response.status_code == 200

@pytest.fixture()
def fake_data():
    faker = Faker()
    payload = {
        "login": faker.user_name(),
        "password": faker.password(),
        "firstName": faker.first_name()
    }
    return payload

@pytest.fixture()
def courier_without_del():
    login, password, first_name = register_new_courier_and_return_login_password()
    login_response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", data={"login": login, "password": password})
    assert login_response.status_code == 200
    new_courier_id = login_response.json()['id']
    yield {
        'id': new_courier_id,
        'login': login,
        'password': password,
        'firstName': first_name
    }