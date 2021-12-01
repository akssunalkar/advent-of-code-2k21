from pathlib import Path
from typing import List
from utils import open_file

file_path = Path("problem_1/p_1_1.txt")
input_measurements = [
    int(val) for val in open_file(file_path=file_path, as_list_values=True)
]


def compare_count_increase(list_values: List[int]) -> int:
    increase_counter = 0
    prev_pointer = 0
    while prev_pointer < len(list_values) - 1:
        curr_value = list_values[prev_pointer]
        next_value = list_values[prev_pointer + 1]
        if curr_value < next_value:
            increase_counter += 1
        prev_pointer += 1
    return increase_counter


## Part1
num_increase = compare_count_increase(list_values=input_measurements)
print(f"Part 1: {num_increase}")
## Part2

slide_3_measurements = [
    sum(input_measurements[i : i + 3]) for i in range((len(input_measurements) - 2))
]
num_increase_sliding = compare_count_increase(list_values=slide_3_measurements)
print(f"Part 2: {num_increase_sliding}")
