import os
import streamlit as st

st.markdown("# 云恒数据打标 🎉")
st.sidebar.markdown("# 标签导航 🎉")

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
