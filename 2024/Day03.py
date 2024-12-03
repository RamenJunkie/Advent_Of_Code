import re
# https://www.w3schools.com/python/python_regex.asp
# https://regex101.com/

with open("Day03Input.txt") as file:
    data = file.read()

rxstring = "mul\(\d+,\d+\)"
rxstring2 = "mul\(\d+,\d+\)|do\(\)|don't\(\)"
total = 0
total2 = 0
enabler = True

def multiplier(a,b):
   return int(a)*int(b)

valid = re.findall(rxstring2,data)

for each in valid:
#   print(each)
   if "don't()" in each:
     enabler = False
   elif "do()" in each:
     enabler = True
   else:
     digits = re.findall('\d+',each)
     value = multiplier(digits[0],digits[1])
     total += value
     if enabler:
       total2 += value

print(total)
print(total2)

#Part1 - 179571322
#Part2 - 103811193
