import re

with open("Day08_Input.txt") as file:
    literals = file.read()

def count_encoded(s):
    length = 2
    for char in s:
        if char in ('"', "\\"):
            length += 2
        else:
            length += 1
    return length


string_2 = 0
encoded_memory = 0
string_memory = 0
total_memory = 0
literals = literals.split("\n")

for each in literals:
    each = each.rstrip()
    total_memory += len(each)
    string_memory += len(eval(each))
    encoded_memory += count_encoded(each)

print(f"Total Memory: {total_memory}")
print(f"Strimg Memory: {string_memory}")
print(f"Encoded Memory: {encoded_memory}")
print(f"Difference: {total_memory-string_memory}")
print(f"Difference2: {encoded_memory-total_memory}")


## 1641 TOO HIGH
## 1041 Too Low
## Correct Part 1 1342

##Part2
## 645 Too Low
## 1987 Too Low