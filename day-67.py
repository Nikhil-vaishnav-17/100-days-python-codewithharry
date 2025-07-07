#Library management question
class Library:
    def __init__(self, library_name:str):
        self.__library_name = library_name
        self.__books = dict()
        self.__noOfBooks = 0

    def addBooks(self, *book_names:str):
        for book_name in book_names:
            if not book_name in self.__books.values():
                self.__noOfBooks += 1
                self.__books[self.__noOfBooks] = book_name
                print(f'{book_name} added to {self.__library_name} at {self.__noOfBooks}')
            else:
                print(f'{book_name} is already present')

    def printLibName(self):
        print(f'The library name is: {self.__library_name}')

    def showBooksName(self):
        print('The name of all the books are: ')
        for keys in self.__books:
            print(f'{keys} : {self.__books[keys]}')

    def totalBooks(self):
        print(f'Total books in the {self.__library_name} is {self.__noOfBooks}')

if __name__ == '__main__':
    lib_name = str(input('Enter the library name: '))
    lib = Library(lib_name)
    while True:
        try:
            print('\n1 for library name\n2 for add book\n3 for show books\n4 for show no of books\n0 for exit.')
            user_input = int(input('Enter the choice:'))
            match user_input:
                case 0:
                    break
                case 1:
                    lib.printLibName()
                    continue
                case 2:
                    name = input('Enter book name: ')
                    lib.addBooks(name)
                    continue
                case 3:
                    lib.showBooksName()
                    continue
                case 4:
                    lib.totalBooks()
                    continue
                case _:
                    raise ValueError
        except ValueError:
            print('Not a valid choice')