from pathlib import Path
from utils import open_file

direction_counter = {"forward": 0, "up": 0, "down": 0}

directions_value = [
    line.strip().split()
    for line in open_file(file_path=Path("problem_2/p2.txt"), as_list_values=True)
]
# Part1
for d, val in directions_value:
    direction_counter[d] += int(val)
final_location = direction_counter["forward"] * (
    direction_counter["down"] - direction_counter["up"]
)
print(final_location)

# Part2
aim = 0
horizontal = 0
depth = 0
for d, val in directions_value:
    x = int(val)
    if d == "forward":
        horizontal += x
        depth += aim * x
    elif d == "up":
        aim -= x
    else:
        aim += x
print(horizontal, depth, horizontal * depth)
