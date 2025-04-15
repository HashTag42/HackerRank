# HackerRank challenge: https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true

#!/bin/python3

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apples_in_house = 0
    oranges_in_house = 0
    for apple in apples:
        fall = a + apple
        if fall >= s and fall <= t:
            apples_in_house += 1
    print(apples_in_house)
    oranges_in_house = 0
    for orange in oranges:
        fall = b + orange
        if fall >= s and fall <= t:
            oranges_in_house += 1
    print(oranges_in_house)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
