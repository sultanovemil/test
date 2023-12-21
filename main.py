import streamlit as st
import os

a = os.getenv('API_K')
#a = st.secrets['API_K']
if a == 'hello':
  st.success('good')  
else: 
  st.success('bad')
  
