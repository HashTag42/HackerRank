# HackerRank: 30 Days of Code - Day 3: Intro to Conditional Statements
# Problem: https://www.hackerrank.com/challenges/30-conditional-statements?isFullScreen=true

if __name__ == '__main__':
    N = int(input().strip())
    if N % 2 == 1:
        print("Weird")
    else:
        if N >= 2 and N <= 5:
            print("Not Weird")
        elif N >= 6 and N <= 20:
            print("Weird")
        elif N >20:
            print("Not Weird")
