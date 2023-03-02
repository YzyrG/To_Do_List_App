"""
TO_DO_List GUI style
"""

import time
import todos_functions
import PySimpleGUI as psg

psg.theme('DarkGreen')

# 第一行
time_label = psg.Text(key="time")  # app标题
massage = psg.Text(key="massage", text_color="red")  # 给用户提示信息
# 第二行
input_box = psg.InputText(tooltip="Enter todo", key="todo")  # 输入框
add_button = psg.Button("Add")
# 第三行
list_box = psg.Listbox(values=todos_functions.get_todos(), key="todos",
                       enable_events=True, size=[45, 10])
edit_button = psg.Button("Edit")
finish_button = psg.Button("Finish")
# 第四行
exit_button = psg.Button("Exit")

window = psg.Window("My Todo App",
                    # layout形参， 实参必须是迭代器如list, list中包含其他list, 一个list占一行
                    layout=[[time_label, massage],
                            [input_box, add_button],
                            [list_box, edit_button, finish_button],
                            [exit_button]],
                    font=("Helvetica", 12))
while True:
    event, values = window.read(timeout=500)  # 显示window
    window['time'].update(value=time.strftime("%Y-%m-%d %H:%M:%S"))  # 显示当前时间
    # print(event)
    # print(values)
    match event:
        case "Add":
            todos = todos_functions.get_todos()
            todo = values["todo"].strip().lower() + '\n'
            todos.append(todo)
            todos_functions.put_todos(to_dos=todos)
            window['todos'].update(values=todos)  # 输完新的todo点击Add后将新的todos显示在list_box中
        case "Edit":
            try:
                todo_before = values["todos"][0]   # values字典的key "todos"拿到的value是个列表，所以还需要再用index取一下
                todo_new = values["todo"]

                todos = todos_functions.get_todos()
                index = todos.index(todo_before)
                todos[index] = todo_new + '\n'  # 新的todo在输入框中编辑，所以其内容对应key:'todo'
                todos_functions.put_todos(todos)
                window['todos'].update(values=todos)  # 输完新的todo点击Edit后将新的todos显示在list_box中
                window['todo'].update(value=' ')  # 注意这里的参数是value单数形式
            except IndexError:
                window['massage'].update(value="You should select a todo first!")
        case "Finish":
            try:
                todos = todos_functions.get_todos()
                todo_delete = values['todos'][0]
                todos.remove(todo_delete)
                todos_functions.put_todos(todos)
                window['todos'].update(values=todos)  # 删除todo后更新listbox
                window['todo'].update(value=' ')  # 注意这里的参数是value单数形式
            except IndexError:
                psg.popup("You should select a todo first!")
        case "Exit":
            break
        case "todos":  # 点击listbox中的某个todo时event是todos
            window['todo'].update(value=values["todos"][0].strip('\n'))  # 点击list_box中的某个todo时直接将该todo显示在input_box中
        case psg.WIN_CLOSED:
            break  # break只结束while循环，而exit() 直接结束整个程序，不再执行下面的语句


window.close()  # 关闭window

