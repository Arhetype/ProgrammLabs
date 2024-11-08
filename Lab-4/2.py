print("Номер варианта:", (17 - 1) % 3 + 1)

from enum import Enum
import math
import random

class Topic(Enum):
    SCIENCE = 1
    HISTORY = 2
    LITERATURE = 3
    ART = 4
    MUSIC = 5

class Book:
    def __init__(self, title, author, topic):
        self.title = title
        self.author = author
        self.topic = topic

books = [
    Book("The Origin of Species", "Charles Darwin", Topic.SCIENCE),
    Book("A Brief History of Time", "Stephen Hawking", Topic.SCIENCE),
    Book("The Guns of August", "Barbara Tuchman", Topic.HISTORY),
    Book("The Decline and Fall of the Roman Empire", "Edward Gibbon", Topic.HISTORY),
    Book("Moby-Dick", "Herman Melville", Topic.LITERATURE),
    Book("To Kill a Mockingbird", "Harper Lee", Topic.LITERATURE),
    Book("The Picture of Dorian Gray", "Oscar Wilde", Topic.ART),
    Book("The Da Vinci Code", "Dan Brown", Topic.ART),
    Book("Beethoven: The Music and the Life", "Lewis Lockwood", Topic.MUSIC),
    Book("The Rest is Noise", "Alex Ross", Topic.MUSIC)
]

def create_book_sets(n, books):
    num_books = len(books)
    books_per_set = int(math.ceil(num_books / n))

    random.shuffle(books)

    book_sets = []

    for i in range(n):
        start = i * books_per_set
        end = (i + 1) * books_per_set
        book_sets.append(books[start:end])

        topics = {}
        for book in book_sets[i]:
            if book.topic not in topics:
                topics[book.topic] = 0
            topics[book.topic] += 1

        max_topic_books = max(topics.values())

        for topic in Topic:
            if topic in topics:
                num_topic_books = topics[topic]
                num_missing_books = max_topic_books - num_topic_books
                for j in range(num_missing_books):
                    for k in range(num_books):
                        if books[k].topic == topic and books[k] not in book_sets[i]:
                            book_sets[i].append(books[k])
                            break

    return book_sets

if __name__ == '__main__':
    a = int(input("Введите ко-во книжных наборов: "))
    book_sets = create_book_sets(a, books)
    for i, book_set in enumerate(book_sets):
        print(f"Book set {i+1}:")
        for book in book_set:
            print(f"- {book.title} by {book.author} ({book.topic.name})")