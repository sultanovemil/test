import streamlit as st
import os

a = os.getenv('API_KR')
#a = st.secrets['API_KR']
if a == 'hello':
  st.success('good')
  st.success('ok')
else: 
  st.success('bad')
  
