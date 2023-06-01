import http

import pytest
import requests


@pytest.mark.parametrize('param', {1, 2, 3})
def test_list_breweries(param):
    """Проверка получения заводов по заданным параметрам"""
    request = requests.get("https://api.openbrewerydb.org/v1/breweries", params={"per_page": str(param)})
    assert request.status_code == http.HTTPStatus.OK


def test_show_all_metadata():
    """Проверка получения мета данных по всем закодам"""
    request = requests.get("https://api.openbrewerydb.org/v1/breweries/meta")
    assert request.status_code == http.HTTPStatus.OK


@pytest.mark.parametrize('param,param2', [(1, "micro"), (2, "nano"), (3, "large")])
def test_list_breweries_2(param, param2):
    """Проверка получения заводов по нескольким заданным параметрам"""
    request = requests.get("https://api.openbrewerydb.org/v1/breweries", params={"by_type": param2,
                                                                                 "per_page": str(param)})
    assert request.status_code == http.HTTPStatus.OK


def test_show_random_breweries():
    """Проверка получения случайного завода"""
    request = requests.get("https://api.openbrewerydb.org/v1/breweries/random")
    assert request.status_code == http.HTTPStatus.OK


@pytest.mark.parametrize('param', {1, 2, 3})
@pytest.mark.parametrize('param2', {'dog', 'sea', 'brew'})
def test_list_breweries_3(param, param2):
    """Проверка получения заводов по поисковому слову"""
    request = requests.get("https://api.openbrewerydb.org/v1/breweries", params={"query": param2,
                                                                                 "per_page": str(param)})
    assert request.status_code == http.HTTPStatus.OK
