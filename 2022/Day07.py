with open("Day07Input.txt") as file:
    data = file.read()

split = data.split('\n')
tree_dict = {"/": 0}
current_dir = []

for each in split:
    cl = each.split(" ")
    if cl[0] == "$":
        if cl[1] == "cd":
            if cl[2] == "/":
                current_dir = ["/"]
            elif cl[2] == "..":
                current_dir.pop()
            else:
                current_dir.append(cl[2])
    elif cl[0] == "dir":
        tree_dict["".join(current_dir)+cl[1]] = 0
    else:
        for tree_walker in range(0,len(current_dir)):
            tree_dict["".join(current_dir[0:tree_walker+1])] += int(cl[0])
    # print(current_dir)
    # print(files)

# print(tree_dict)

space_needed = 30000000 - (70000000-tree_dict['/'])
size_to_delete = tree_dict["/"]
total_size = 0
for key in tree_dict.keys():
    if tree_dict[key] <= 100000:
        total_size += tree_dict[key]
    if tree_dict[key] > space_needed and tree_dict[key] < size_to_delete:
        size_to_delete = tree_dict[key]

print(total_size)
# 6199378 high
# 1048940 low
# 1145908 low

print(size_to_delete)

##Part 1: 1582412
##Part 2: 3696336
