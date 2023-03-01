import todos_functions
import PySimpleGUI as psg

label = psg.Text("Type in a todo")  # app标题
input_box = psg.InputText(tooltip="Enter todo", key="todo")  # 输入框
add_button = psg.Button("Add")
list_box = psg.Listbox(values=todos_functions.get_todos(), key="todos",
                       enable_events=True, size=[45, 10])
edit_button = psg.Button("Edit")


window = psg.Window("My Todo App",
                    # layout形参， 实参必须是迭代器如list, list中包含其他list, 一个list占一行
                    layout=[[[label],
                             [input_box, add_button],
                             [list_box, edit_button]]],
                    font=("Helvetica", 12))
while True:
    event, values = window.read()  # 显示window
    print(event)
    print(values)
    match event:
        case "Add":
            todos = todos_functions.get_todos()
            todo = values["todo"].strip().lower() + '\n'
            todos.append(todo)
            todos_functions.put_todos(to_dos=todos)
            window['todos'].update(values=todos)  # 输完新的todo点击Add后将新的todos显示在list_box中
        case "Edit":
            todo_before = values["todos"][0]   # values字典的key "todos"拿到的value是个列表，所以还需要再用index取一下
            todo_new = values["todo"]

            todos = todos_functions.get_todos()
            index = todos.index(todo_before)
            todos[index] = todo_new + '\n'  # 新的todo在输入框中编辑，所以其内容对应key:'todo'
            todos_functions.put_todos(todos)
            window['todos'].update(values=todos)  # 输完新的todo点击Edit后将新的todos显示在list_box中
        case "todos":  # 点击listbox中的某个todo时event是todos
            window['todo'].update(value=values["todos"][0].strip('\n'))  # 点击list_box中的某个todo时直接将该todo显示在input_box中
        case psg.WIN_CLOSED:
            break


window.close()  # 关闭window

