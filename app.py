import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(layout="wide")

# index.html 파일을 읽어서 출력
with open("dashboard/index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1000, scrolling=True)
