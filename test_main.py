import os

from streamlit.testing.v1 import AppTest

def test_fun():
    at = AppTest.from_file('main.py', default_timeout=30)
    at.secrets['API_K'] = os.getenv('API_K')
    at.run()   
    assert at.success[0].value == 'good'
