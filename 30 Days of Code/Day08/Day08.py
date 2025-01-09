# HackerRank 30 days of code Day 8: Dictionaries and Maps
# Problem: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':

    n = int(input().strip())

    dict = {}

    for i in range(0,n):
        entry = list(map(str, input().rstrip().split()))
        dict[entry[0]] = entry[1]

    try:
        while True:
            name = input()
            if name != "":
                if name in dict:
                    print(f"{name}={dict[name]}")
                else:
                    print("Not found")
            else:
                break
    except EOFError:
        pass