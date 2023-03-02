"""
To_Do_List Web style
"""

import streamlit as st  # streamlit 是开源的web前端框架
import todos_functions

todos = todos_functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'  # st.session_state是字典，'new_todo'是它的一个key
    todos.append(todo)
    todos_functions.put_todos(todos)
    # print(todo)


st.title("My Todo App")
st.subheader("This is my todo app!")
st.write("You can manage your todos in this app :)")

for todo in todos:
    todo = todo.strip('\n')
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a new todo.",
              on_change=add_todo, key="new_todo")