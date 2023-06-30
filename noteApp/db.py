import view


def add_data(full_data):
    with open("file.json", "a", encoding="UTF-8") as file:
        file.write(full_data)


def find_post(find_str):
    with open("file.json", "r+", encoding="UTF-8") as file:
        list_str = file.readlines()
        list_worker = []
        for worker in list_str:
            list_worker.append(worker)
        for i in range(len(list_worker)):
            if find_str == i:
                print(list_worker[i])


def remove_post():
    with open("file.json", "r+", encoding="UTF-8") as file:
        list_str = file.readlines()
        list_worker = []
        for worker in list_str:
            list_worker.append(worker)
            print(worker)

    with open("file.json", "w", encoding="UTF-8") as file:
        number = int(
            input('Enter the number of the entry to be deleted(starts from 0): '))
        for i in range(len(list_worker)):
            if number == i:
                continue
            file.writelines(list_worker[i])
    print("Done!")


def export_all_data():
    with open("file.json", "r", encoding="UTF-8") as file:
        list_str = file.readlines()
        for worker in list_str:
            print(worker)


def delete_all_data():
    with open("file.json", "w", encoding="UTF-8") as file:
        print("Done!")


def change_data():
    with open("file.json", "r+", encoding="UTF-8") as file:
        list_str = file.readlines()
        list_worker = []
        for worker in list_str:
            list_worker.append(worker)
            print(worker)

    with open("file.json", "w", encoding="UTF-8") as file:
        number = int(
            input('Enter the number of the entry that should be modified(starts from 0): '))
        for i in range(len(list_worker)):
            if number == i:
                list_worker[i] = view.get_data()
            file.writelines(list_worker[i])
    print("Done!")
