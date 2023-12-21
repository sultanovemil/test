import os

from streamlit.testing.v1 import AppTest

def test_fun():
  at = AppTest.from_file('main.py', default_timeout=30)
  at.secrets['API_KR'] = os.getenv('API_KR')
  at.run()   
  assert at.success[0].value == 'good'
  assert at.success[1].value == 'ok'

