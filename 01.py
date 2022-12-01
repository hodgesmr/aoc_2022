import heapq
from utils import timed, get_input_lines


# Loop over all the calories
# When we hit a blank value, sum, and then compare to a running max
def part_1(input_lines):
    max_calories = 0
    current_elf_total = 0

    for c in input_lines:
        if c and c != "\n":
            current_elf_total += int(c)
        else:
            if current_elf_total > max_calories:
                max_calories = current_elf_total
            current_elf_total = 0

    return max_calories


# Loop over all the calories
# When we hit a blank value, sum, and push into a heap
# Then pop thrice off the heap, and sum that
def part_2(input_lines):
    elf_calorie_heap = []
    current_elf_total = 0

    for c in input_lines:
        if c and c != "\n":
            current_elf_total += int(c)
        else:
            # it's a min-heap, so negate the total before pushing
            heapq.heappush(elf_calorie_heap, -1 * current_elf_total)
            current_elf_total = 0

    top_3_sum = 0
    for i in range(3):
        # de-negate the value from the min-heap, and add
        top_3_sum += -1 * heapq.heappop(elf_calorie_heap)

    return top_3_sum


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
