"""
To_Do_List Web style
"""

import streamlit as st  # streamlit 是开源的web前端框架
import todos_functions


todos = todos_functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app!")
st.write("You can manage your todos in this app :)")

for todo in todos:
    todo = todo.strip('\n')
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a new todo.")