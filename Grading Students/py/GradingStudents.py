# HackerRank challenge: Grading Students
# https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true

#!/bin/python3

import os

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for g in range(len(grades)):
        grade = grades[g]
        if grade >= 38:
            next5 = nextMultipleOfFactor(grades[g], 5)
            if next5 - grade < 3:
                grades[g] = next5
    return grades

def nextMultipleOfFactor(num, factor):
    for i in range (factor):
        target = num + i
        if (target % factor) == 0:
            return target

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

