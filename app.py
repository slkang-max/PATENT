import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide", page_title="My Dashboard")

current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "dashboard", "index.html")

try:
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    components.html(html_content, height=1000, scrolling=True)

except FileNotFoundError:
    st.error(f"파일을 찾을 수 없습니다: {html_path}")
    st.info("GitHub에 'dashboard' 폴더와 'index.html' 파일이 잘 올라갔는지 확인해주세요.")
