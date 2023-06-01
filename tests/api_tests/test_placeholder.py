import http

import pytest
import requests

creating_dto = {
    "title": 'foo12',
    "body": 'bar23',
    "userId": 34,
}

updating_dto = {
    "id": 1,
    "title": 'foooof',
    "body": 'barer',
    "userId": 134,
}


@pytest.mark.parametrize('param', {1, 2, 3})
def test_get_user(param):
    """Проверка получения информации о пользователе"""
    request = requests.get("https://jsonplaceholder.typicode.com/todos/" + str(param))
    assert request.status_code == http.HTTPStatus.OK


def test_create_post():
    """Поверка возможности создания поста"""
    request = requests.post("https://jsonplaceholder.typicode.com/posts", json=creating_dto)
    assert request.status_code == http.HTTPStatus.CREATED


def test_update_post():
    """Поверка возможности обновления поста"""
    request = requests.put("https://jsonplaceholder.typicode.com/posts/2", json=updating_dto)
    assert request.status_code == http.HTTPStatus.OK


@pytest.mark.parametrize('param', {1, 2, 3})
def test_get_post(param):
    """Поверка получения информации о заданном посте"""
    request = requests.get("https://jsonplaceholder.typicode.com/posts/" + str(param))
    assert request.status_code == http.HTTPStatus.OK


@pytest.mark.parametrize('param', {1, 2, 3})
def test_get_album(param):
    """Поверка получения информации о заданном альбоме"""
    request = requests.get("https://jsonplaceholder.typicode.com/albums/" + str(param))
    assert request.status_code == http.HTTPStatus.OK
