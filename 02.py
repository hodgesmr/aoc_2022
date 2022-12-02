from utils import timed, get_input_lines


def part_1(input_lines):
    opponent_codes = ["A", "B", "C"]
    my_codes = ["X", "Y", "Z"]
    my_code_scores = [1, 2, 3]
    outcome_scores = [0, 3, 6]

    total_score = 0
    for line in input_lines:
        opponent, me = line.split(" ")
        opponent_index = opponent_codes.index(opponent)
        my_index = my_codes.index(me)
        my_score = my_code_scores[my_index]

        outcome_score = outcome_scores[(my_index - opponent_index + 1) % 3]

        round_score = my_score + outcome_score
        total_score += round_score

    return total_score


def part_2(input_lines):
    opponent_codes = ["A", "B", "C"]
    outcome_codes = ["X", "Y", "Z"]
    my_code_scores = [1, 2, 3]
    outcome_scores = [0, 3, 6]

    total_score = 0
    for line in input_lines:
        opponent, me = line.split(" ")
        opponent_index = opponent_codes.index(opponent)
        outcome_index = outcome_codes.index(me)
        outcome_score = outcome_scores[outcome_index]

        my_score = my_code_scores[(opponent_index + (outcome_score // 3) -1) % 3]

        round_score = my_score + outcome_score
        total_score += round_score

    return total_score


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
