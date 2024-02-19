from library import Library


def main():
    lib = Library()

    while True:
        print("\n*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4)Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            title = input("Enter the title of the book to remove: ")
            lib.remove_book(title)
        elif choice == "4":
            exit()
        elif choice == "q":
            exit()
        elif choice == "Q":
            exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
