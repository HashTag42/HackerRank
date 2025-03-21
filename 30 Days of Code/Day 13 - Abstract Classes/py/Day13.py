# HackerRank: 30 Days of Code: Day 13: Abstract Classes
# Problem: https://www.hackerrank.com/challenges/30-abstract-classes/problem

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price
    def display(self):
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Price: {price}")


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()