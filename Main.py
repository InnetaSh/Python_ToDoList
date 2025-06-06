import json
from datetime import datetime

filePath = "ToDoList.txt"

def load_notes():
    try:
        with open(filePath, "r", encoding="utf-8") as myfile:
            data = myfile.read()
            if data:
                notes = json.loads(data)
            else:
                notes = []
    except FileNotFoundError:
        notes = []
    except Exception as ex:
        print(f"Ошибка при загрузке: {ex}")
        notes = []
    return notes


def  save_notes(notes):
    try:
        with open(filePath, "w", encoding="utf-8") as myfile:
            json.dump(notes, myfile, ensure_ascii=False, indent=4)
    except Exception as ex:
        print(f"Ошибка при сохранении: {ex}")



def list_notes(notes):
    if not notes:
        print("\n Нет сохранённых заметок.")
        return
    i = 0
    idx = 1
    for note in notes:
        print(f"\nЗаметка #{idx}")
        print(f"  Title: {note['title']}")
        print(f"  Text: {note['text']}")
        print(f"  Status: {note['status']}")
        print(f"  Data: {note['data']}")
        idx += 1
        print("-----------------------------------------")


def info_contact():
    note = {}
    note['title'] = input("Введите title: ")
    note['text'] = input("Введите text: ")
    while True:
        status_input = input("Введите статус (1 - сделано, 2 - не сделано): ")
        if status_input == '1':
            note['status'] = 'сделано'
            break
        elif status_input == '2':
            note['status'] = 'не сделано'
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите 1 или 2.")
    note['data'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return note

def add_note(notes):
    note = info_contact()
    notes.append(note)
    print("Заметка добавлена.")
    print("-----------------------------------------")



def subMenu(note):

    while True:
        print("Выберите данные заметки для изменения:")
        print("1. Изменить title")
        print("2. Изменить text")
        print("3. Изменить status")
        print("4. В меню")
        choice = input("Выберите действие: ")
        match choice:
            case  "1":
                title = input("Введите title: ")
                note['title'] = title
            case  "2":
                text = input("text: ")
                note['text'] = text
            case  "3":
                while True:
                    status_input = input("Введите статус (1 - сделано, 2 - не сделано): ")
                    if status_input == '1':
                        note['status'] = 'сделано'
                        break
                    elif status_input == '2':
                        note['status'] = 'не сделано'
                        break
                    else:
                        print("Некорректный ввод. Пожалуйста, выберите 1 или 2.")
            case "4":
                break
            case _:
                print("Неверный выбор. Попробуйте снова.")



def  update_note(notes):
    list_notes(notes)
    if not notes:
        return
    idx = int(input("\nВведите номер заметки для изменения: ")) - 1
    if 0 <= idx < len(notes):
        subMenu(notes[idx])
        print(" заметки обновлёны.")
    else:
        print(" Неверный номер заметки.")




def  delete_note(notes):
    list_notes(notes)
    if not notes:
        return
    idx = int(input("\nВведите номер заметки для удаления: ")) - 1
    if 0 <= idx < len(notes):
        del notes[idx]
        print(" Контакт удалён.")
    else:
        print("Неверный номер заметки.")





def  search_note_by_title(notes):
    query = input("Введите часть title для поиска: ").strip().lower()
    if not query:
        print("Пустой запрос.")
        return

    results = []
    for note in notes:
        if query in note['title'].lower():
            results.append(note)

    if results:
        print(f"\nНайдено заметок: {len(results)}")
        list_notes(results)
    else:
        print("Заметки не найдены.")
    input("Нажмите Enter для продолжения...")


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
                print("Заметки сохранены. Выход.")
                break
            case "6":
                search_note_by_title(notes)
            case _:
                print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()