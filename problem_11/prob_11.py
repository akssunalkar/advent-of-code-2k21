from collections import defaultdict
import numpy as np
from scipy.sparse import dok_matrix
from utils import open_file
from pathlib import Path
from copy import deepcopy


# sample_data = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526"""

sample_data = open_file(file_path=Path("problem_11/p_11.txt"), as_list_values=True)
OCTOPUS_MAP = defaultdict(lambda: 100)
n_r = set()
n_col = set()
for x, line in enumerate(sample_data):
    n_r.add(x)
    for y, energy_level in enumerate(line.strip()):
        OCTOPUS_MAP[(x, y)] = int(energy_level)
        n_col.add(y)

NUM_ROWS = len(n_r)
NUM_COLS = len(n_col)


def get_adjacent_indices(point):
    x, y = point
    return [
        (x, y - 1),
        (x, y + 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x + 1, y + 1),
    ]


def increment_map(pos_map, num_rows, num_cols, pos_points=None):
    if pos_points:
        for i, j in pos_points:
            pos_map[(i, j)] += 1
    else:
        for i in range(num_rows):
            for j in range(num_cols):
                pos_map[(i, j)] += 1
    return pos_map


def flash_map(pos_map, seen_points, flash_count):
    points_to_flash = [k for k, v in pos_map.items() if 9 < v < 100]
    flash_count += len(points_to_flash)
    neighbors = [get_adjacent_indices(p) for p in points_to_flash]
    if points_to_flash:
        for p, p_neighbors in zip(points_to_flash, neighbors):
            if p not in seen_points:
                pos_map[p] = 0
                seen_points.add(p)
            else:
                continue
            for n in p_neighbors:
                if n not in seen_points:
                    pos_map[n] += 1

        return flash_map(
            pos_map=pos_map, seen_points=seen_points, flash_count=flash_count
        )
    else:
        return pos_map, flash_count


def part1(octopus_map):
    total_flash_count = 0
    step = 0
    while step < 100:
        step_flash_count = 0
        octopus_map = increment_map(octopus_map, NUM_ROWS, NUM_COLS)
        octopus_map, flash_count = flash_map(
            pos_map=octopus_map, seen_points=set(), flash_count=step_flash_count
        )
        total_flash_count += flash_count
        step += 1
    return total_flash_count


def part2(octopus_map):
    step = 0
    while True:
        step_flash_count = 0
        octopus_map = increment_map(octopus_map, NUM_ROWS, NUM_COLS)
        octopus_map, flash_count = flash_map(
            pos_map=octopus_map, seen_points=set(), flash_count=step_flash_count
        )
        if flash_count == (NUM_ROWS * NUM_COLS):
            break
        step += 1
    return step + 1


# Part1
total_flash_count = part1(octopus_map=deepcopy(OCTOPUS_MAP))
print(total_flash_count)

# Part2
step_for_all_flash = part2(octopus_map=OCTOPUS_MAP)
print(step_for_all_flash)
