with open("Day05Input.txt") as file:
    data = file.read()

split_data = data.split('\n\n')
crates = split_data[0].split('\n')
moves = split_data[1].split('\n')

def pivot(crates):
    crates.pop(-1)
    processed = []
    for row in crates:
        row = row.replace('    ', ' [ ]')
        # print(len(row))
        while len(row) < len(crates[-1]):
            row += ' [ ]'
        row = row[1:-1].split('] [')
        # print(row)
        processed.append(row)
    # print(processed)
    return list(zip(*processed[::-1]))

def drop_blanks(crates):
    de_blanked = []
    for crate in crates:
        row = [i for i in crate if i != ' ']
        de_blanked.append(row)
    return de_blanked

def move_crates(crate_move, moves):
    for move in moves:
        steps = move.split(" ")
        how_many = int(steps[1])
        from_stack = int(steps[3])-1
        to_stack = int(steps[5])-1
        for i in range(0,how_many):
            # print(crate_move[from_stack])
            # print(crate_move[to_stack])
            crate_move[to_stack].append(crate_move[from_stack].pop())
        #print(steps)
    return crate_move

def move_crates_in_stacks(crates_stack, moves):
    for move in moves:
        steps = move.split(" ")
        how_many = int(steps[1])
        from_stack = int(steps[3])-1
        to_stack = int(steps[5])-1
        #print(crates_stack[from_stack])
        move_list = crates_stack[from_stack][-how_many:]
        #print(crates_stack[to_stack])
        for i in range(how_many):
            crates_stack[from_stack].pop()
            crates_stack[to_stack].append(move_list[i])
        #print(steps)
    return crates_stack

crates = pivot(crates)
crates = drop_blanks(crates)
#Part 1
#moved = move_crates(crates, moves)
moved2 = move_crates_in_stacks(crates, moves)

print(crates)
#print(len(crates))
#print(moves)

#Part 1
# for each in moved:
#     print(each[-1])
#svfdLGLWV

for each in moved2:
    print(each[-1])
#DCVTCVPCL