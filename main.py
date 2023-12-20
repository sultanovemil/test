import streamlit as st
import os

a = os.getenv('API_K')
st.text_area(key='ta', value='hi')
if a == 'hello':
  st.success('ok')
  st.text_area(key='ta', value='good')
  
