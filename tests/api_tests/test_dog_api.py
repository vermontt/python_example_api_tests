import http

import pytest
import requests


@pytest.mark.parametrize("param", ["affenpinscher", "african", "akita"])
def test_breeds_list(param):
    """Проверка получения случайного
     изображения заданной породы собаки"""
    request = requests.get('https://dog.ceo/api/breed/' + param + '/images/random')
    assert request.status_code == http.HTTPStatus.OK


def test_list_all_sub_breeds():
    """Проверка получения списка собак определенной породы"""
    request = requests.get('https://dog.ceo/api/breed/hound/list')
    assert request.status_code == http.HTTPStatus.OK


def test_all_breeds():
    """Проверка получения списка всех пород"""
    request = requests.get("https://dog.ceo/api/breeds/list/all")
    assert request.status_code == http.HTTPStatus.OK


@pytest.mark.parametrize("param", [3, 2, 1])
def test_multiple_images(param):
    """Проверка получения нескольких изображений одной породы собаки"""
    request = requests.get('https://dog.ceo/api/breeds/image/random/' + str(param))
    assert request.status_code == http.HTTPStatus.OK


def test_list_all_sub_breeds_images():
    """Проверка получения изображений конкретной собаки"""
    request = requests.get('https://dog.ceo/api/breed/hound/afghan/images')
    assert request.status_code == http.HTTPStatus.OK
