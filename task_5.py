import json
import os


LIBRARY_FILE = "library.json"

#проверка на файл
if not os.path.exists(LIBRARY_FILE):
    with open(LIBRARY_FILE, "w") as f:
        json.dump([], f, indent=4)


#функция для загрузки книг из JSON
def load_books():
    with open(LIBRARY_FILE, "r") as f:
        return json.load(f)


#сохранения книг
def save_books(books):
    with open(LIBRARY_FILE, "w") as f:
        json.dump(books, f, indent=4)


#просмотр книг
def view_books():
    books = load_books()
    if not books:
        print("Книги отсутствуют.")
        return
    for book in books:
        print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Статус: {book['status']}")


#поиск
def search_books(keyword):
    books = load_books()
    found = [book for book in books if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower()]
    if not found:
        print("Совпадений не найдено.")
        return
    for book in found:
        print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Статус: {book['status']}")


#добавление новой книги
def add_book(title, author):
    books = load_books()
    new_id = max([book['id'] for book in books], default=0) + 1
    books.append({"id": new_id, "title": title, "author": author, "status": "доступна"})
    save_books(books)
    print("Книга добавлена.")


#изменение статуса книги
def change_status(book_id, new_status):
    books = load_books()
    for book in books:
        if book['id'] == book_id:
            book['status'] = new_status
            save_books(books)
            print("Статус обновлён.")
            return
    print("Книга с таким ID не найдена.")


#удаление
def delete_book(book_id):
    books = load_books()
    new_books = [book for book in books if book['id'] != book_id]
    if len(books) == len(new_books):
        print("Книга с таким ID не найдена.")
        return
    save_books(new_books)
    print("Книга удалена.")


#экспорт в текстовый файл
def export_available_books():
    books = load_books()
    available = [book for book in books if book['status'] == "доступна"]
    with open("available_books.txt", "w") as f:
        for book in available:
            f.write(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}\n")
    print("Доступные книги экспортированы в available_books.txt.")


#меню
def menu():
    while True:
        print("\n1. Просмотр всех книг")
        print("2. Поиск книги")
        print("3. Добавить книгу")
        print("4. Изменить статус книги")
        print("5. Удалить книгу")
        print("6. Экспорт доступных книг")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            view_books()
        elif choice == "2":
            keyword = input("Введите название или автора: ")
            search_books(keyword)
        elif choice == "3":
            title = input("Название книги: ")
            author = input("Автор книги: ")
            add_book(title, author)
        elif choice == "4":
            book_id = int(input("ID книги: "))
            status = input("Новый статус (доступна/взята): ")
            change_status(book_id, status)
        elif choice == "5":
            book_id = int(input("ID книги: "))
            delete_book(book_id)
        elif choice == "6":
            export_available_books()
        elif choice == "0":
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


#запуск
if __name__ == "__main__":
    menu()