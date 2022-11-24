with open("Day07_Input.txt") as file:
    bitwise = file.read()

operations = bitwise.split('\n')

op_dict = {}

for each in operations:
    each_list = each.split(" -> ")
    op_dict[each_list[1]] = each_list[0]

## PART 2 Override Wire B to the result of A from part 1
op_dict["b"] = 3176

print(op_dict['a'])

def get_value(key):
    entry = op_dict[key]
    if str(entry).isnumeric():
        op_dict[key] = int(entry)
        return int(entry)
    else:
        if "NOT" in entry:
            value = get_value(entry.split(" ")[1])
            return_val = 65536 + ~value
        elif len(entry.split(" ")) == 1:
             return_val = get_value(entry)
        else:
            biteq = entry.split(" ")
            if str(biteq[0]).isnumeric():
                val1 = int(biteq[0])
            else:
                val1 = get_value(biteq[0])

            if str(biteq[2]).isnumeric():
                val2 = int(biteq[2])
            else:
                val2 = get_value(biteq[2])


            if biteq[1] == "AND":
                return_val = (val1 & val2)
            elif biteq[1] == "OR":
                return_val = (val1 | val2)
            elif biteq[1] == "LSHIFT":
                return_val = (val1 << val2)
            elif biteq[1] == "RSHIFT":
                return_val = (val1 >> val2)
        #print(return_val)
        op_dict[key] = int(return_val)
        return return_val

# for each in op_dict:
#     op_dict[each] = get_value(op_dict[each])

op_dict["a"] = get_value("a")

# print(op_dict)
print(op_dict['a'])
## 3176


## Part 2
## 14710
