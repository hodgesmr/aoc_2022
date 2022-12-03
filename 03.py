from utils import timed, get_input_lines
import string


# Loop over every rucksack
# Get each compartment by taking each half and storing as a set
# Find the intersection of the two sets, this is guaranteed to be one item
# Score and sum
def part_1(input):
    priority_sum = 0
    for rucksack in input:
        compartment_1 = set(rucksack[: len(rucksack) // 2])
        compartment_2 = set(rucksack[len(rucksack) // 2 :])
        common = compartment_1.intersection(compartment_2).pop()
        if common in string.ascii_lowercase:
            ascii_offset = 96
        else:
            ascii_offset = 38

        priority = ord(common) - ascii_offset

        priority_sum += priority

    return priority_sum


# Loop over every rucksack
# Keep a rolling list of the 3 most recent rucksacks
# Represent each rucksack as a set
# Find the intersection of the three sets, this is guaranteed to be one item
# Score and sum
def part_2(input):
    priority_sum = 0
    current_group = []
    for rucksack in input:
        current_group.append(set(rucksack))
        if len(current_group) == 3:
            common = (current_group[0] & current_group[1] & current_group[2]).pop()
            if common in string.ascii_lowercase:
                ascii_offset = 96
            else:
                ascii_offset = 38

            priority = ord(common) - ascii_offset
            priority_sum += priority
            current_group.clear()
    return priority_sum


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
