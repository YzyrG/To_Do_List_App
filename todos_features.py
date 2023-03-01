"""
To_Do_List_App 功能
"""
# from todos_func import get_todos, put_todos
import todos_functions
import time

#  显示当前时间
now = time.strftime("%Y-%m-%d %H:%M:%S")
print(now)

while True:
    # 得到用户输入并去除多余空格以小写形式赋给变量user_action
    user_action = input("Type add, edit, complete, show or exit: ").strip().lower()

    # 新增
    if user_action.startswith("add"):
        todos = todos_functions.get_todos()

        todo = user_action[4:] + '\n'
        todos.append(todo)  # 将用户输入的todo加入todos list
        # print(todos)

        todos_functions.put_todos(to_dos=todos)
    # 编辑
    elif user_action.startswith("edit"):
        try:
            todos = todos_functions.get_todos()

            number = int(user_action[5:]) - 1
            todos[number] = input("enter your edit: ").lower() + '\n'
            # print(todos)
            print(f"Number {number + 1} was edit successes!")

            todos_functions. put_todos(to_dos=todos)
        except ValueError:  # 处理因用户输入不匹配的数据类型时导致的ValueError
            print("Hi! Your command is not valid. ")
            continue
    # 显示所有todo
    elif user_action.startswith("show"):
        todos = todos_functions.get_todos()  # todos中每个元素尾部都有'\n'

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item[:-1].title()}"  # item[:-2]去除行间多余的空行
            print(row)  # print函数会自动换行
    # 删除已完成todo
    elif user_action.startswith("complete"):
        try:
            todos = todos_functions.get_todos()

            number = int(user_action[9:]) - 1
            complete_todo = todos.pop(number).strip('\n')
            print(f"[{complete_todo.title()}] was removed from the list!")

            todos_functions.put_todos(to_dos=todos)
        except ValueError:
            print("Hi! Your command is not valid. ")
            continue
    # 退出
    elif user_action.startswith("exit"):
        break
    else:
        print("Hi, you entered an unknown command.")

print("Bye!")


