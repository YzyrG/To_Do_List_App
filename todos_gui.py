import todos_functions
import PySimpleGUI as psg

label = psg.Text("Type in a todo")  # app标题
input_box = psg.InputText(tooltip="Enter todo", key="todo")  # 输入框
add_button = psg.Button("Add")

window = psg.Window("My Todo App",
                    # layout形参， 实参必须是迭代器如list, list中包含其他list, 一个list占一行
                    layout=[[[label], [input_box, add_button]]],
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
        case psg.WIN_CLOSED:
            break


window.close()  # 关闭window

