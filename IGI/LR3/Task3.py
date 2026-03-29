"""
Task1 - analize text count symbols in range 'g' and 'o'
Author: Zhebrik German
Date: 25-03-2026
"""

def count_characters_in_range(text, start_char='g', end_char='o'):
    count = 0
    for char in text:
        if start_char <= char <= end_char:
            count += 1
    return count

def main():
    text = input("Enter text: ")
    print("Count elems > g and < o = ", count_characters_in_range(text))
main()