from utils import get_input_lines, timed


def find_first_unique_substring(signal, length):
    for i in range(len(signal)):
        if i >= length and len(set(signal[i-length:i])) == length:
            return i


def part_1(input):
    return find_first_unique_substring(input[0], 4)


def part_2(input):
    return find_first_unique_substring(input[0], 14)


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
