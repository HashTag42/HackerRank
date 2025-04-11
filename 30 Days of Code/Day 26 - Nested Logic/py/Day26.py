# HackerRank: 30 Days of Code: Day 26 Nested Logic
# Problem: https://www.hackerrank.com/challenges/30-nested-logic/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

import datetime

def getDate(string):
    # Split the string into components
    day, month, year = map(int, string.split())
    date = datetime.date(year, month, day)
    return date

def calc_fine(ret_date, due_date):
    fine = None
    if ret_date <= due_date:
        fine = 0
    elif ret_date.year == due_date.year and ret_date.month == due_date.month:
        fine = 15 * (ret_date.day - due_date.day)
    elif ret_date.year == due_date.year:
        fine = 500 * (ret_date.month - due_date.month)
    elif ret_date.year > due_date.year:
        fine = 10000

    return fine

return_date = getDate(input())
due_date = getDate(input())
fine = calc_fine(return_date, due_date)
print(fine)