# HackerRank: 30 Days of Code: Day 10: Binary Numbers
# Problem: https://www.hackerrank.com/challenges/30-binary-numbers/problem

if __name__ == '__main__':
    n = int(input().strip())

    b = bin(n)[2:]

    l = 0
    maximum = 0
    streak = False
    for i in range(0,len(b)):
        digit = int(b[i])
        if not streak and digit == 1:
            streak = True
            l = 1
        elif streak is True and digit == 1:
            l +=1
        elif streak is True and digit == 0:
            streak = False
            maximum = max(maximum, l)

    maximum = max(maximum, l)

    print(maximum)