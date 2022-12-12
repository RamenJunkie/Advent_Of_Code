import math
import json

with open("Day11Input.txt") as file:
    data = file.read()

split = data.split("\n\n")

monkies = {}

for each in split:
    each = each.replace('Monkey ', '{"')
    each = each.replace(': ', '": "')
    each = each.replace('\n  ', '", "')
    each = each.replace(':", "Starting ', '": {"')
    each = each.replace('new = old ', '')
    each = each.replace('divisible by ', '')
    each = each.replace('  If t', 'T')
    each = each.replace('  If f', 'F')
    each = each.replace('throw to monkey ', '')
    each = each + '"}}'
    monkies.update(json.loads(each))

monkey_list = monkies.keys()
num_monks = len(monkey_list)

# Part1
# rounds = 20
# Part2
rounds = 10000

common_multiple = 1
# print(monkies['3'])
for monk in range(0, num_monks):
    monkies[str(monk)]["item_count"] = 0
    monkies[str(monk)]["items"] = ", "+monkies[str(monk)]["items"]
    common_multiple *= int(monkies[str(monk)]["Test"])

for i in range(rounds):
    for monk in range(0, num_monks):
        # print(monk)
        items = monkies[str(monk)]["items"].split(", ")
        # print(items)
        if len(items) > 0:
            for item in items[1:]:
                monkies[str(monk)]["item_count"] += 1
                operations = monkies[str(monk)]["Operation"].split(" ")
                if operations[1] == "old":
                    # Part 1
                    # test_case = math.floor((int(item) * int(int(item)))/3)
                    # Part 2
                    test_case = math.floor((int(item) * int(int(item))))
                elif operations[0] == "*":
                    # Part 1
                    # test_case = math.floor((int(item) * int(operations[1]))/3)
                    # Part 2
                    test_case = math.floor((int(item) * int(operations[1])))
                else:
                    # Part 1
                    # test_case = math.floor((int(item) + int(operations[1]))/3)
                    # Part 2
                    test_case = math.floor((int(item) + int(operations[1])))
                if test_case % int(monkies[str(monk)]["Test"]) == 0:
                    throw_to = monkies[str(monk)]["True"]
                else:
                    throw_to = monkies[str(monk)]["False"]
                monkies[throw_to]["items"] = monkies[throw_to]["items"] + ", "+str(test_case%common_multiple)
        monkies[str(monk)]["items"] = ""

# print(monkies)

item_counts = []
for monk in range(0, num_monks):
    item_counts.append(monkies[str(monk)]["item_count"])

item_counts.sort(reverse=True)
print(item_counts[0]*item_counts[1])
# 25738411485