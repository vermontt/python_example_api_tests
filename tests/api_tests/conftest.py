import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="Base url"
    )

    parser.addoption(
        "--status",
        default=200,
        help="Expected status code"
    )

    parser.addoption(
        "--method",
        default="get",
        help="method"
    )


@pytest.fixture()
def base_url(request):
    return request.config.getoption(name="--url")


@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption(name="--method"))


@pytest.fixture()
def status_code(request):
    return request.config.getoption(name="--status")
