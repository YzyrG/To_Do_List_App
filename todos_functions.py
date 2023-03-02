"""
To_Do_List_App  Functions
"""

FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """将已有文件:todos中的内容读入todos变量, 并返回此list"""
    with open(filepath, 'r') as file_before:
        todos_before = file_before.readlines()
    return todos_before


def put_todos(to_dos, filepath=FILEPATH):
    """将新的todos list写入文件,无返回"""
    todos_new = to_dos
    with open(filepath, 'w') as file_now:
        file_now.writelines(todos_new)


if __name__ == "__main__":
    print(get_todos())

