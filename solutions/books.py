class Library:
    def __init__(self, books=None):
        self.no_books = 0
        self.books = []

        if books is not None:
            if isinstance(books, list):
                self.books.extend(books)
                self.no_books += len(books)
            else:
                self.books.append(books)
                self.no_books += 1

    def add_book(self, book_name):
        if not (book_name in self.books):
            self.books.append(book_name)
            self.no_books += 1
        else:
            print(f"The book {book_name} is already in the library")

    def add_books(self, *books_list):
        self.books.extend(books_list)
        self.no_books += len(books_list)

    def show_books(self):
        i = 1
        for book in self.books:
            print(f"{i}. {book}")
            i += 1

    def show_no_books(self):
        print(f"Number of books = {self.no_books}")

    def check_no_books(self):
        if len(self.books) == self.no_books:
            return True
        else:
            return False


l1 = Library()
l2 = Library('Art')
l3 = Library(['Art', 'Eldia'])
l1.add_books("48 laws of power", "style", 'Tree')
l1.add_book("Horizon")

l1.show_books()
l1.show_no_books()
print(f"Check = {l1.check_no_books()}")
