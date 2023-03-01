import todos_functions
import PySimpleGUI as psg

label = psg.Text("Type in a todo")  # app标题
input_box = psg.InputText(tooltip="Enter todo")  # 输入框
add_button = psg.Button("Add")

# layout形参， 实参必须是迭代器如list, list中包含其他list, 一个list占一行
window = psg.Window("My todo app", layout=[[[label], [input_box, add_button]]])
window.read()  # 显示window
window.close()  # 关闭window

