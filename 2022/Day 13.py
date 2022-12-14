from functools import cmp_to_key

with open("Day13Input.txt") as file:
    data = file.read()

split_data = data.split("\n\n")
decode_data = []
for line in data.replace("\n\n", "\n").split("\n"):
    decode_data.append(eval(line))

def compare_lists(left,right):
    # print(left)
    # print(right)

    if isinstance(left, int) and isinstance(right, int):
        # print(f"{left} {right}")
        if left < right:
            return 1
        elif left > right:
            return -1
        return 0

    if isinstance(left, list) and isinstance(right, list):
        for value in range(min(len(left), len(right))):
            check_value = (compare_lists(left[value], right[value]))
            # print(f"{left[value]} {right[value]}")
            # print(check_value)
            if check_value != 0:
                return check_value

        if len(left) < len(right):
            return 1
        elif len(left) > len(right):
            return -1
    if isinstance(left, int) and isinstance(right, list):
        return compare_lists([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return compare_lists(left, [right])

    return 0

## Not Used But This really feels like it should have worked.
def decoder(decode_list):
    new_list = []
    for each in decode_list:
        each = each.replace("[]", "0")
        each = each.replace("[", "")
        each = each.replace("]", "")
        each = each.replace(",", "")
        new_list.append(int(each[0]))
    new_list.sort()
    print(new_list)
    print((new_list.index(6)+1)*(new_list.index(2)+1))

index_sum = 0
for i in range(len(split_data)-1):
    set1 = split_data[i].split("\n")[0]
    set2 = split_data[i].split("\n")[1]

    match = compare_lists(eval(set1), eval(set2))
    # print(match)

    if match == 1:
        index_sum += (i+1)


print(index_sum)
# 6373 Too high
# 5997 Too low
# 6187

decode_data.append([[2]])
decode_data.append([[6]])
#decoder(decode_data)
decode_data.sort(key=cmp_to_key(compare_lists), reverse=True)
# for each in decode_data:
#     print(each)
print((decode_data.index([[2]])+1)*(decode_data.index([[6]])+1))

# 23520