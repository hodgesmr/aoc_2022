import inspect
import os
import time


def timed(func):
    t_start = time.perf_counter()
    result = func()
    t_end = time.perf_counter()
    print(f"{func.__name__} ({(t_end - t_start):0.6f} seconds) : {result}")



# I know this is gross but leave me alone
def get_input_lines():
    script_file = inspect.stack()[1].filename
    day = os.path.splitext(os.path.basename(script_file))[0]
    data_path = f"input/{day}.txt"
    puzzle_data_lines = []
    with open(data_path, "r") as puzzle_data_file:
        for line in puzzle_data_file:
            puzzle_data_lines.append(line)

    return puzzle_data_lines
