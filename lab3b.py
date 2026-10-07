# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: 
# Usage: ./lab3b.py

# Follow the specific instructions given in the README.md file

def reverse_list(values):
    left = 0
    right = len(values) - 1
    while left < right:
        values[left], values[right] = values[right], values[left]
        left = left + 1
        right = right -1

numbers = [1, 4, 9, 25, 37, 44, 74, 89, 101, 56]

print("Before:", numbers)
reverse_list(numbers)
print("After:", numbers)