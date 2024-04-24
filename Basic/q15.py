#  Chocolate Purchase Calculation with Discounts: Develop a program that calculates the total number of chocolates a person can buy, given the cost per chocolate, the amount of money they have, and a discount scheme based on wrappers returned.

cost = float(input("Enter the cost of a chocolate: "))
money = float(input("Enter the amount of money you have: "))
wrappers = int(input("Enter the number of wrappers you have: "))
discount = int(input("Enter the number of wrappers required for a free chocolate: "))
chocolates = money // cost
wrappers += chocolates
while wrappers >= discount:
    free = wrappers // discount
    chocolates += free
    wrappers = wrappers % discount + free

print(f"You can buy {chocolates} chocolates.")