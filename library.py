class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def add_book(self):
        with open(self.file_name, "a+") as file:
            book_title = input("Enter the book title: ")
            book_author = input("Enter the book author: ")
            release_year = input("Enter the first release year: ")
            num_pages = input("Enter the number of pages: ")

            book_info = f"{book_title},{book_author},{release_year},{num_pages}\n"
            file.write(book_info)
            print("Book added successfully.")

    def list_books(self):
        with open(self.file_name, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                book_info = line.split(',')
                book_title = book_info[0]
                book_author = book_info[1]
                print(f"Book Title: {book_title}, Author: {book_author}")

    def remove_book(self, title):
        with open(self.file_name, "r") as file:
            lines = file.readlines()
        with open(self.file_name, "w") as file:
            for line in lines:
                if title not in line:
                    file.write(line)
            print(f"Book '{title}' removed successfully.")
