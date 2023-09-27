import library_database_module

def main_menu():
    while True:
        print("Welcome to the library management system!")
        print("Please select what you want to do:")
        print("1. Add new books")
        print("2. Find book Details")
        print("3. Find scheduled status")
        print("4. View all books")
        print("5. Modify book details")
        print("6. Delete book")
        print("7. Exit")

        choice = input()

        if choice == "1":
            add_a_book()
        elif choice == "2":
            find_book_details()
        elif choice == "3":
            find_reservation_status()
        elif choice == "4":
            view_all_books()
        elif choice == "5":
            modify_book_details()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            break
        else:
            print("Invalid selection, please re-enter.")

def add_a_book():
    print("Please enter new book information:")
    book_title = input("Title:")
    book_author = input("Author:")
    book_isbn = input("ISBN：")

    library_database_module.add_book(book_title, book_author, book_isbn)

def find_book_details():
    book_id = input("Please enter the book ID:")
    result = library_database_module.get_book_detail(book_id)
    if result:
        print(result)
    else:
        print("Can't find the book, please make sure the ID is correct.")

def find_reservation_status():
    input_string = input("Please enter the book ID, title, user ID, or reservation ID:")
    if input_string.startswith("LB"):
        result = library_database_module.get_reservation_by_id(input_string[2])
    elif input_string.startswith("LU"):
        result = library_database_module.get_reservation_by_user(input_string[2:])
    elif input_string.startswith("LR"):
        result = library_database_module.get_reservation_by_id(input_string[2:])
    else:
        result = library_database_module.get_reservation_by_title(input_string)

    if result:
        print(result)
    else:
        print("No relevant information can be found, please confirm that the input is correct.")

def view_all_books():
    result = library_database_module.get_books_detail()
    if result:
        for item in result:
            print(item)
    else:
        print("No books were found.")

def modify_book_details():
    book_id = input("Please enter the ID of the book you want to modify:")
    new_title = input("Please enter a new title:")
    new_author = input("Please enter a new author name:")
    new_isbn = input("Please enter a new ISBN:")
    new_status = input("Please enter a new status:")
    if new_status !=None:
        new_user_id = input("Please enter a new user ID:")
        success = library_database_module.update_book_status(book_id, new_title, new_author, new_isbn, new_status, new_user_id)
    else:
        success = library_database_module.update_book(book_id, new_title, new_author, new_isbn)
    if success:
        print("Modified successfully!")
    else:
        print("Can't find the book, please make sure the ID is correct.")

def delete_book():
    book_id = input("Please enter the ID of the book you want to delete:")
    success = library_database_module.delete_book(book_id)
    if success:
        print("Successfully deleted！")
    else:
        print("Can't find the book, please make sure the ID is correct.")

if __name__ == "__main__":
    main_menu()
