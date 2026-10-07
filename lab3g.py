# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: 
# Usage: ./lab3g.py

# Follow the specific instructions given in the README.md file
numbers = []
while len(numbers) < 6:
    value = input("Enter a number: ")
    value = int(value)
    numbers.append(value)
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 10
numbers.reverse()
print(numbers)
