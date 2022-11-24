vowels = ['a','e','i','o','u']
bad_string = ['ab', 'cd', 'pq', 'xy']
number_of_nice = 0
different_nice = 0

with open("Day05_Input.txt") as file:
    names = file.read()

names_list = names.split('\n')

def check_once(name):
    for each in bad_string:
        if each in name:
            return False
    return True

def check_twice(name):
    total_vowels = 0
    for each in vowels:
        for i in name:
            if each == i:
                total_vowels += 1

    if total_vowels >= 3:
        return True
    return False

def check_thrice(name):
    for each in range(len(name) - 1):
        if name[each] == name[each+1]:
            return True
    return False

for each_name in names_list:
    if check_once(each_name):
        if check_twice(each_name):
            if check_thrice(each_name):
                number_of_nice += 1

print(number_of_nice)

# Part 1 Answer
#255

# Part 2 - New Rules
def check_fourth(name):
    for each in range(len(name) - 1):
        check_string = name[each]+name[each+1]
        # print(f'{check_string} | {name}')
        # print(f'{check_string} | {name[:each]}**{name[each+2:]}' )
        if check_string in name[:each] or check_string in name[each+2:]:
            # print(f'{check_string} | {name}')
            # print(f'{check_string} | {name[:each]}**{name[each + 2:]}')
            return True
    # print("Nope1")
    return False

def check_fifth(name):
    for each in range(len(name) - 2):
        if name[each] == name[each+2]:
            # print(f'{name[each]} | {name[each+2]}')
            return True
    # print("Nope2")
    return False

for each_name in names_list:
    if check_fourth(each_name):
        if check_fifth(each_name):
            #print(each_name)
            different_nice +=1

print(different_nice)

# Part 2
# 15 is wrong
# 177 too high
# 77 is wrong
## 55 is the answer