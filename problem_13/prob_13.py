from collections import defaultdict
from utils import open_file
from pathlib import Path

data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
manual = open_file(file_path=Path("problem_13/pr_13.txt"), as_list_values=True)
point_map = defaultdict(lambda: 0)
NUM_ROWS = 0
NUM_COLS = 0
instructions = []
instruction_counter = 0
for line in manual:
    if not line.strip():
        continue
    if "fold" in line:
        l = line.strip("fold along ")
        instructions.append(l.split("="))
    else:
        coord = line.strip().split(",")
        x, y = int(coord[0]), int(coord[1])
        point_map[(y, x)] = 1
        if y > NUM_ROWS:
            NUM_ROWS = y
        if x > NUM_COLS:
            NUM_COLS = x

print(instructions, NUM_ROWS, NUM_COLS)
temp_map = point_map.copy()
new_map = point_map.copy()

for fold_axis, fold_point in instructions:
    fold_point = int(fold_point.strip())
    if fold_axis == "y":
        for y in range(NUM_ROWS, fold_point, -1):
            for x in range(NUM_COLS + 1):
                if temp_map[(y, x)] == 1:
                    folded_y = (2 * fold_point) - y
                    new_map[(folded_y, x)] = 1
                    new_map.pop((y, x))
    if fold_axis == "x":
        for x in range(NUM_COLS, fold_point, -1):
            for y in range(NUM_ROWS + 1):
                if temp_map[(y, x)] == 1:
                    folded_x = (2 * fold_point) - x
                    new_map[(y, folded_x)] = 1
                    new_map.pop((y, x))
    temp_map = new_map.copy()

max_row = 0
max_col = 0
for loc in new_map:
    if loc[0] > max_row:
        max_row = loc[0]
    if loc[1] > max_col:
        max_col = loc[1]

display = ""
for i in range(max_row + 1):
    temp = []
    for j in range(max_col + 1):
        if new_map[(i, j)]:
            temp.append("#")
        else:
            temp.append(" ")
    temp.append("\n")
    display += "".join(temp)
print(display)
