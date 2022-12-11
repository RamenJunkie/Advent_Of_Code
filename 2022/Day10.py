import math

with open("Day10Input.txt") as file:
    data = file.read()

moves = data.split('\n')

def make_display(pixels,lines):
    display = []
    display_line = []
    for n in range(pixels):
        display_line.append(" ")
    for i in range(lines):
        display.append(display_line.copy())
    return display

def show_display(display):
    for each in display:
        print("".join(each))
    print("\n")

signal_strengths = [0, 1]
cycles = 0
signal = 1 # X In the instructions
line = 0

display = make_display(40, 6)

for move in moves:
    command = move.split(" ")
    signal_strengths.append(signal)
    if command[0] == "noop":
        rangeend = 2
    else:
        rangeend = 3
    for p in range(1, rangeend):
        cycles += 1
        pixel = (cycles)%40
        line = math.floor((cycles)/40)

        if p == 2:
            signal += int(command[1])
            signal_strengths.append(signal)
        first = signal - 1
        last = signal + 1
        if first < 0:
            first = 39
            line -= 1
        if last > 39:
            last = 0
            line += 1
        if pixel in [first, signal, last]:
            display[line][pixel] = "#"

check_values = [20, 60, 100, 140, 180, 220]
total = 0
for each in check_values:
    # print(f"{signal_strengths[each-1]} | {signal_strengths[each]} | {signal_strengths[each]}")
    total += each * signal_strengths[each]
print(total)
# 14060

show_display(display)
## PAPKFKEJ