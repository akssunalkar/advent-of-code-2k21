from utils import open_file
from pathlib import Path
import numpy as np
from collections import defaultdict

from itertools import product

# data = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# """
data = open_file(file_path=Path("problem_9/pr_9.txt"), as_list_values=True)
HEIGHT_MAP = defaultdict(lambda: 100)

rows = set()
cols = set()
for x, line in enumerate(data):
    rows.add(x)
    for y, height in enumerate(line.strip()):
        HEIGHT_MAP[(x, y)] = int(height)
        cols.add(y)

NUM_ROWS = len(rows)
NUM_COLS = len(cols)


def get_minimum_height(height_map: dict):
    minimum_height = []
    minimum_height_index = []
    for x in range(NUM_ROWS + 1):
        for y in range(NUM_COLS + 1):
            pointer = height_map[(x, y)]
            locality = [
                height_map[(i, j)]
                for i, j in product(range(x - 1, x + 2), range(y - 1, y + 2))
            ]
            # locality.remove(pointer)
            if min(locality) == pointer and min(locality) != 100:
                minimum_height.append(pointer)
                minimum_height_index.append((x, y))
    return minimum_height, minimum_height_index


# Part1
min_heights, min_heights_index = get_minimum_height(height_map=HEIGHT_MAP)
total_risk = sum([(h + 1) for h in min_heights])
print(total_risk)


def get_basins_per_point(point_location, seen_set):
    curr_x, curr_y = point_location
    left, right, top, down = [
        (curr_x, curr_y - 1),
        (curr_x, curr_y + 1),
        (curr_x - 1, curr_y),
        (curr_x + 1, curr_y),
    ]
    seen_set.add(point_location)

    if HEIGHT_MAP[left] < 9 and left not in seen_set:
        seen_set.add(left)
        seen_set = get_basins_per_point(left, seen_set)

    if HEIGHT_MAP[right] < 9 and right not in seen_set:
        seen_set.add(right)
        seen_set = get_basins_per_point(right, seen_set)

    if HEIGHT_MAP[top] < 9 and top not in seen_set:
        seen_set.add(top)
        seen_set = get_basins_per_point(top, seen_set)

    if HEIGHT_MAP[down] < 9 and down not in seen_set:
        seen_set.add(down)
        seen_set = get_basins_per_point(down, seen_set)

    return seen_set


# Part2
basin_lengths = []
for min_pos in min_heights_index:
    basin = get_basins_per_point(point_location=min_pos, seen_set=set())
    basin_lengths.append(len(basin))

sorted_basin = sorted(basin_lengths, reverse=True)
final_value = np.product(sorted_basin[:3])
print(final_value)
