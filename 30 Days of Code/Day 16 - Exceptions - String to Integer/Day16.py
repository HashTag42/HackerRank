# HackerRank: 30 Days of Code: Day 16: Exceptions - String to Integer
# Problem: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem?isFullScreen=true

S = input().strip()

try:
    number = int(S)
    print(number)
except ValueError:
    print("Bad String")