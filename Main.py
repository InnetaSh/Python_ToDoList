
def load_notes():
    print("test.")


def list_notes(notes):
    print("test.")


def add_note(notes)
    print("test.")


def  update_note(notes):
    print("test.")


def  delete_note(notes):
    print("test.")


def  save_notes(notes):
    print("test.")


def  search_note_by_title(notes):
    print("test.")


def main():
    notes = load_notes()

    while True:
        print("\nВаши заметки")
        print("1. Показать все заметки")
        print("2. Добавить заметку")
        print("3. Изменить заметку")
        print("4. Удалить заметку")
        print("5. Сохранить и выйти")
        print("6. Поиск заметки по заглавию")
        choice = input("Выберите действие: ")
        match choice:
            case "1":
                list_notes(notes)
            case "2":
                add_note(notes)
                save_notes(notes)
            case "3":
                update_note(notes)
                save_notes(notes)
            case "4":
                delete_note(notes)
                save_notes(notes)
            case "5":
                save_notes(notes)
                print("Контакты сохранены. Выход.")
                break
            case "6":
                search_note_by_title(notes)
            case _:
                print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()