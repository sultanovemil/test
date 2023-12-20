import os
from streamlit.testing import TestClient

def test_my_app():
    # Получаем значение секрета из переменной окружения
    api_key = os.environ['API_K']

    # Создаем клиент для тестирования Streamlit приложения
    client = TestClient('main')

    # Используем полученное значение секрета в тесте
    response = client.get('/my_endpoint', headers={'API_K': api_key})

    # Проверяем ожидаемый результат
    assert response.status_code == 200
