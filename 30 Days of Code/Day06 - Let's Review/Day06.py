# HackeRank: 30 Days of Code - Day 6: Let's Review
# Problem: https://www.hackerrank.com/challenges/30-review-loop/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

def split(S):
    evens = ""
    odds  = ""
    for i in range (0, len(S)):
        if i % 2 == 0:  # index is even
            evens += S[i]
        else:           # index is odd
            odds  += S[i]
    print(evens + " " + odds)



if __name__ == "__main__":
    T = int(input())
    for i in range (0,T):
        S = input()
        split(S)
