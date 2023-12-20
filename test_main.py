import os
from streamlit.testing.v1 import TestClient

def test_my_app():
    # Получаем значение секрета из переменной окружения
    api_key = os.environ['API_K']

    # Создаем клиент для тестирования Streamlit приложения
    client = TestClient('main')
    assert client.sucess[0] == 'ok'
