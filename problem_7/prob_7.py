from utils import open_file
from pathlib import Path
import numpy as np
from tqdm import tqdm

# data="16,1,2,0,4,2,7,1,2,14"
data = open_file(file_path=Path("problem_7/pr_7.txt"), as_list_values=True)

positions = sorted([int(x) for x in data[0].split(",")])


def find_optimum_pos(position_list: list, linear: bool = True) -> float:
    total = []
    for i in tqdm(range(max(position_list))):
        if linear:
            values = sum([abs(x - i) for x in position_list])
        else:
            values = sum([sum(range(abs(x - i) + 1)) for x in position_list])
        total.append(values)
    minimum_fuel = total[np.argmin(total)]
    return minimum_fuel


# part 1
part1_opt_fuel_needed = find_optimum_pos(position_list=positions, linear=True)
print(f"Part1 fuel needed: {part1_opt_fuel_needed}")

# part 2
part2_opt_fuel_needed = find_optimum_pos(position_list=positions, linear=False)
print(f"Part2 fuel needed: {part2_opt_fuel_needed}")
