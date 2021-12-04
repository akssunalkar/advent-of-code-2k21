from utils import open_file
from pathlib import Path
import numpy as np
from collections import Counter
from typing import List
import copy

arr = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
invert_map = {"0": "1", "1": "0"}


def get_most_common_across_string_pos(string_list: List[str]) -> List[str]:
    binary_array = np.array(
        [[x for x in string_num.strip()] for string_num in string_list]
    ).T
    most_common_values_count = []
    for row in binary_array:
        count = Counter(row)
        if count["1"] == count["0"]:
            most_common_values_count.append("1")
        else:
            most_common_values_count.append(count.most_common(1)[0])
    return [val[0] for val in most_common_values_count]


binary_measurements = open_file(
    file_path=Path("problem_3/p_3.txt"), as_list_values=True
)
# binary_measurements=arr.split()
# Part1

common_count = get_most_common_across_string_pos(string_list=binary_measurements)
most_common_values = "".join([val[0] for val in common_count])
opposite = "".join([invert_map[bit] for bit in most_common_values])
most_common_number = int(most_common_values, 2)
least_common_number = int(opposite, 2)
print(most_common_values, opposite, most_common_number * least_common_number)

# Part2


numbers = {num.strip() for num in binary_measurements}
idx = 0
numbers_to_check = copy.deepcopy(binary_measurements)
while True:
    subset = set()
    most_common = get_most_common_across_string_pos(numbers_to_check)[idx]
    for n in binary_measurements:
        if n[idx] == most_common:
            subset.add(n.strip())
    numbers = numbers & subset
    numbers_to_check = numbers
    idx += 1
    if len(numbers_to_check) == 1:
        break

final_num_1 = int(list(numbers)[0], 2)
numbers_new = {num.strip() for num in binary_measurements}
idx_new = 0
numbers_to_check_new = copy.deepcopy(binary_measurements.copy())
while True:
    subset = set()
    most_common = get_most_common_across_string_pos(numbers_to_check_new)[idx_new]
    least_common = invert_map[most_common]
    for n in binary_measurements:
        if n[idx_new] == least_common:
            subset.add(n.strip())
    numbers_new = numbers_new & subset
    numbers_to_check_new = numbers_new
    idx_new += 1
    if len(numbers_to_check_new) == 1:
        break

final_num_2 = int(list(numbers_new)[0], 2)

print(final_num_1, final_num_2, final_num_1 * final_num_2)
