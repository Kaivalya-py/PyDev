#  Count Unique Numbers in a List: Given a list L, create a dictionary where keys are unique numbers from the list, and values are counts of those numbers. Display a set of unique numbers from the list.

def count_unique_numbers(L):
    unique_numbers = set(L)
    counts = {}
    for num in unique_numbers:
        counts[num] = L.count(num)
    print("Unique numbers:", unique_numbers)
    print("Counts:", counts)

L = [1, 2, 3, 4, 1, 2, 3, 4, 5]
count_unique_numbers(L)

