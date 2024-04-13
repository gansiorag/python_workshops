from dataclasses import dataclass


class RegularBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author


@dataclass
class Book:
    # Важно отметить, что аннотации типов обязательны. Все поля, которые не
    # имеют отметок о типе будут проигнорированы. Конечно, если вы не хотите
    # использовать конкретный тип, вы можете указать Any из модуля typing.
    # Что же вы получаете в результате? Вы автоматически получаете класс,
    # с реализованными методами __init__, __repr__, __str__ и __eq__.
    # Кроме того, это будет обычный класс и вы можете наследоваться от него
    # или добавлять произвольные методы.

    title: str
    author: str


if __name__ == '__main__':
    book = Book(title="Fahrenheit 451", author="Bradbury")
    print(book)
    print(book.author)
