# HackerRank: 30 Days of Code - Day 2: Operators
# Problem: https://www.hackerrank.com/challenges/30-operators/problem?isFullScreen=true

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip = meal_cost * float(tip_percent/100)
    tax = meal_cost * float(tax_percent/100)
    tot = meal_cost + tax + tip
    print(round(tot))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
