#  Symmetric Difference Between Two Lists: Implement a program that takes two lists, converts them into sets, and then displays the symmetric difference between the two sets.

def symmetric_difference():
    A = set(input("Enter elements of list A: ").split())
    B = set(input("Enter elements of list B: ").split())
    print("Symmetric Difference:", A.symmetric_difference(B))

symmetric_difference()
