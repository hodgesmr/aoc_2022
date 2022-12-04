from utils import timed, get_input_lines


# Loop over all the assignment pairs
# Extract the text range descriptors of each
# Convert each to a set of the given range
# Compare each set to see if one is a subset of the other
# Increament if so
def part_1(input):
    fully_contained_count = 0
    for assignment_pair in input:
        assignment_descriptors = assignment_pair.split(",")
        assignments = []
        for assignment_descriptor in assignment_descriptors:
            assignment_min, assignment_max = assignment_descriptor.split("-")
            assignments.append(set(range(int(assignment_min), int(assignment_max) + 1)))
        if assignments[0].issubset(assignments[1]) or assignments[1].issubset(assignments[0]):
            fully_contained_count += 1
    return fully_contained_count


# Loop over all the assignment pairs
# Extract the text range descriptors of each
# Convert each to a set of the given range
# Compare each set to see if one intersects the other
# Increament if so
def part_2(input):
    overlap_count = 0
    for assignment_pair in input:
        assignment_descriptors = assignment_pair.split(",")
        assignments = []
        for assignment_descriptor in assignment_descriptors:
            assignment_min, assignment_max = assignment_descriptor.split("-")
            assignments.append(set(range(int(assignment_min), int(assignment_max) + 1)))
        if assignments[0] & assignments[1]:
            overlap_count += 1
    return overlap_count
    


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
