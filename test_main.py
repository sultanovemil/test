import os

from streamlit.testing.v1 import AppTest
secret_val = os.getenv('API_K')

secrets = {"API_K": os.getenv('API_K')}

def test_url_input():
    at = AppTest.from_file('main.py', default_timeout=30, secrets=secrets) 
    at.run()
    at.secrets['API_K'] 
    assert at.success[0].value == 'good'
