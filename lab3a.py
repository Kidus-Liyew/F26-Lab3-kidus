# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: 
# Usage: ./lab3a.py
import random

numbers = []
for i in range(20):
    numbers.append(random.randint(0, 99))

print("Original Numbers:", numbers)
numbers.sort()
print("Sorted Numbers:", numbers)