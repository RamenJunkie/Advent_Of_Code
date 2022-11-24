
with open("Day06_Input.txt") as file:
    lights = file.read()

instructions = lights.split('\n')

light_array = []
row_array = []

#build array
for n in range(1000):
    row_array.append("O")
for n in range(1000):
    light_array.append(row_array)

def toggle(light):
    if light == 'O':
        return '*'
    return 'O'

def change_lights(array, xstart, ystart, xend, yend, action):
    for ycor in range(ystart,yend):
        for xcor in range(xstart, xend):
            # print(f'{xcor} | {ycor}')
            if action == 'on':
                array[xcor][ycor] = "*"
            elif action == 'off':
                array[xcor][ycor] = "O"
            elif action == 'toggle':
                array[xcor][ycor] = toggle(array[xcor][ycor])

    return array



for each in instructions:
    if 'toggle' in each:
        each = "Turn "+each
    comm = each.split(" ")
    light_array = change_lights(light_array, int(comm[2].split(',')[0]), int(comm[2].split(',')[1]), int(comm[4].split(',')[0]), int(comm[4].split(',')[1]), comm[1])

on_count = 0

print(light_array[0])

for i in light_array:
    print(f'{"".join(i)}')
    with open(file = "Day06_Output.txt", mode='a') as output:
        output.write(f'{"".join(i)}\n')
    for n in i:
        if n == '*':
           on_count+=1

print(light_array[522][730])
print(f"Total lights on = {on_count}")

# 522000 Too High
# 478000 Too high