from utils import get_input_lines, timed



# Helper function to increment x and cycle based on op delta
def increment_and_calculate(x, delta, cycle):
    cycle += 1
    interesting_strength = None
    if cycle == 20 or cycle > 40 and (cycle-20) % 40 == 0:
        interesting_strength = cycle * x
    if delta != 0:
        cycle += 1
        if cycle == 20 or cycle > 40 and (cycle-20) % 40 == 0:
            interesting_strength = cycle * x
        x += delta
    
    return x, interesting_strength, cycle
        

# Helpfer function to find the row, position in row, and sprite positions
# based on cycle and x
def row_position_sprite(cycle, x):
    row = cycle // 40
    position = cycle % 40
    sprite = set({x-1, x, x+1})

    return row, position, sprite


# Loop over all instructions
# update x and cycle based on operation
# record a running list of interesting cycles
# sum at end
def part_1(input):
    interesting_strengths = []
    cycle = 0
    x = 1
    for instruction in input:
        if instruction == 'noop':
            x, strength, cycle = increment_and_calculate(x, 0, cycle)

        else:
            delta = int(instruction.split(" ")[1])
            x, strength, cycle = increment_and_calculate(x, delta, cycle)
 
        if strength:
            interesting_strengths.append(strength)

    return sum(interesting_strengths)


# CRT is a 40*6 two-d array
# Loop over instructions
# Mark the CRT pixel if there's an overlap
# print
def part_2(input):
    crt = [['.']*40 for i in range(6)]
    cycle = 0
    x = 1

    for instruction in input:
        if instruction == 'noop':
            row, position, sprite = row_position_sprite(cycle, x)
            cycle += 1
            if position in sprite:
                crt[row][position] = '#'

        else:
            delta = int(instruction.split(" ")[1])

            # first op
            row, position, sprite = row_position_sprite(cycle, x)
            cycle += 1
            if position in sprite:
                crt[row][position] = '#'

            # second op
            row, position, sprite = row_position_sprite(cycle, x)
            cycle += 1
            if position in sprite:
                crt[row][position] = '#'

            x += delta

    for row in crt:
        print("".join(row))


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
