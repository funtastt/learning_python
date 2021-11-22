"""
Наследование - что же это? И как это? И почему в Python'e нет перегрузки конструктора?
На первые 2 я сейчас отвечу, а на последний не ответит никто.

1. Как работает наследование?
class Book - класс-родиитель
class eBook(Book) - дочерний класс, наследуется от Book

2. Перегрузка конструктора (костыли)

Рассмотрим частный случай - мой код


    def __init__(self, *args):
        если в конструктор передано 5 значений, то передано каждое значение по отдельности,
        инициализируем их по отдельности
        if len(args) == 5:
            super().__init__(args[0], args[1], args[2], args[3])
            self.language = args[4]

        если в конструктор передано 2 значения, то одно из них - уже сформированный родительский класс Book
        а второе - язык.
        if len(args) == 2:
            book = args[0]
            language = args[1]

            super(eBook, self).__init__(book.name, book.release_date, book.author, book.text)
            self.language = language


"""
import datetime


class Book:
    def __init__(self, name, release_date, author, text):
        self.name = name
        self.release_date = release_date
        self.author = author
        self.text = text

    def get_info(self):
        print("Name: " + self.name)
        print("Release date: " + str(self.release_date))
        print("Author: " + self.author)
        print("Text: " + self.text)

    def return_this(self):
        return self


class eBook(Book):
    def __init__(self, *args):
        if len(args) == 5:
            super().__init__(args[0], args[1], args[2], args[3])
            self.language = args[4]

        if len(args) == 2:
            book = args[0]
            language = args[1]

            super(eBook, self).__init__(book.name, book.release_date, book.author, book.text)
            self.language = language

    def get_info(self):
        super(eBook, self).get_info()
        print("Language: " + self.language)


harry_potter = Book("Harry Potter", datetime.date.today(), "Rowling", "Lorem ipsum dolor sit amet")
harry_potter_eBook = eBook(harry_potter, "RUS")
harry_potter_eBook.get_info()
