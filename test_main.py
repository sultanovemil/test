import os

from streamlit.testing.v1 import AppTest

a = os.getenv('API_K')
# Just a simple test
def test_url_input():
    at = AppTest.from_file('main.py', default_timeout=30) 
    at.run()
    assert st.success[0].value == 'ok'
