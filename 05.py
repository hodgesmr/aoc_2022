from collections import deque
import re

from utils import get_input_lines, timed


def stacks_and_moves_from_input(input):
    stacks = [deque() for i in range(9)]  # we've got 9 stacks
    for i, line in enumerate(input):
        if line == "" :  # Once we hit a blank line, we're done parsing the stacks
            return stacks, input[i+1:]
        else:
            stacks_at_level = [line[i+1:i+2] for i in range(0, len(line), 4)]  # list of letters from bracket-y string
            for i, stack_item in enumerate(stacks_at_level):
                if stack_item != " ":
                    stacks[i].appendleft(stack_item)  # appendleft because we're building top down



# Get our ascii stacks as python deques
# Iterate over the moves text, turning into a 3-item list
# Iterate over each list, popping and pushing
def part_1(input):
    stacks, moves_input = stacks_and_moves_from_input(input)
    for line in moves_input:
        moves = [int(s) for s in re.findall(r'\d+', line)]  # extract the ints from our moves
        for _ in range(moves[0]):
            crate = stacks[moves[1]-1].pop()  # Get the crate on the top
            stacks[moves[2]-1].append(crate)  # Push it where it needs to go
    
    # String from the tops of all the stacks
    return "".join([stack[-1] for stack in stacks])


# Get our ascii stacks as python deques
# Iterate over the moves text, turning into a 3-item list
# Iterate over each list, popping and pushing
def part_2(input):
    stacks, moves_input = stacks_and_moves_from_input(input)
    for line in moves_input:
        moves = [int(s) for s in re.findall(r'\d+', line)]  # extract the ints from our moves
        crates_to_move = deque()  # build a new stack that we'll move all at once
        for m in range(moves[0]):
            crate = stacks[moves[1]-1].pop()  # Get the crate on the top
            crates_to_move.appendleft(crate)  # Push left to preserve order
        stacks[moves[2]-1].extend(crates_to_move)  # Push it where it needs to go
    
    # String from the tops of all the stacks
    return "".join([stack[-1] for stack in stacks])
    


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
