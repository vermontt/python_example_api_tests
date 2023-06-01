

def test_ya_ru(base_url, status_code, request_method):
    """Тест с переменными, которые передаются в терминал"""
    response = request_method(url=base_url)
    assert response.status_code == int(status_code)
