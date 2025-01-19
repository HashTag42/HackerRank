# HackerRank: 30 Days of Code: Day 12: Inheritance
# Problem: https://www.hackerrank.com/challenges/30-inheritance/problem

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
        self.grade  = ""

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        total_score = 0
        for score in scores:
            total_score += score
        avg_score = total_score / len(scores)
        if   90 <= avg_score <= 100:
            grade = "O"
        elif 80 <= avg_score <  90:
            grade = "E"
        elif 70 <= avg_score <  80:
            grade = "A"
        elif 55 <= avg_score <  70:
            grade = "P"
        elif 40 <= avg_score <  55:
            grade = "D"
        else:
            grade = "T"
        return grade


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())