import view
import db


def main():
    while True:
        operation = view.get_op()
        if operation == 1:
            data_worker = view.get_data()
            db.add_data(data_worker)

        if operation == 2:
            change = int(input("1 - Entire list\n2 - Selectively\n"))
            if change == 1:
                db.export_all_data()
            else:
                find_str = view.find_post()
                db.find_post(find_str)

        if operation == 3:
            change = int(input("1 - Delete\n2 - Modify\n"))
            if change == 1:
                change = int(
                    input("1 - Delete note\n2 - Delete all notes\n"))
                if change == 1:
                    db.remove_post()
                else:
                    db.delete_all_data()
            else:
                db.change_data()

        if operation == 4:
            break


main()
