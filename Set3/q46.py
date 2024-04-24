#  Count Word Occurrence in a String: Develop a Python program that takes a string as input and counts the occurrence of each word. Display the result in a dictionary format, along with a set of unique words present in the string.

def count_word_occurrence(s):
    words = s.split()
    unique_words = set(words)
    counts = {}
    for word in unique_words:
        counts[word] = words.count(word)
    print("Unique words:", unique_words)
    print("Counts:", counts)

s = input("Enter a string: ")
count_word_occurrence(s)
