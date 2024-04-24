# Set Operations (Union, Intersection, Difference): Write a Python program that takes two sets, A and B, and displays their union, intersection, and difference.

def set_operations():
    A = set(input("Enter elements of set A: ").split())
    B = set(input("Enter elements of set B: ").split())
    print("Union:", A.union(B))
    print("Intersection:", A.intersection(B))
    print("Difference:", A.difference(B))

set_operations()
