def get_op():
    operation = int(input(
        "Choose an option: \n 1 - Add new note \n 2 - Add note from a file \n 3 - Delete/Modify \n 4 - Exit \n"))
    return operation


def get_data():
    name = input("Choose note header: \n")
    body = input("Enter note content: \n")
    full_data = (name + ' ' + body)+"\n"
    return full_data


def find_post():
    data = int(input("Enter article number (starts from 0): "))
    return data
