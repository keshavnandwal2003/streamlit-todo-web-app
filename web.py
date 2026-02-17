import streamlit as st
import functions
import uuid

if "todos" not in st.session_state:
    st.session_state.todos = functions.get_todos()


def add_todo():
    text = st.session_state.new_todo.strip()
    if text:
        new_todo = {
            "id": str(uuid.uuid4()),
            "text": text
        }
        st.session_state.todos.append(new_todo)
        functions.write_todos(st.session_state.todos)
        st.session_state.new_todo = ""


def remove_todo(todo_id):
    st.session_state.todos = [todo for todo in st.session_state.todos if todo["id"] != todo_id]
    functions.write_todos(st.session_state.todos)


st.title("My Todo App")
st.subheader("Increase your productivity 🚀")

for todo in st.session_state.todos:
    st.checkbox(
        todo["text"],
        key=todo["id"],
        on_change=remove_todo,
        args=(todo["id"],)
    )

st.text_input(
    "",
    placeholder="Add new todo...",
    key="new_todo",
    on_change=add_todo
)
