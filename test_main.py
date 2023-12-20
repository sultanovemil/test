import os
from streamlit.testing.v1 import AppTest

def test_url_input():
    at = AppTest.from_file('main.py', default_timeout=30) 
    at.run()    
    assert at.success[0].value == 'ok'
    assert at.text_area(key='ta').value == 'good'
