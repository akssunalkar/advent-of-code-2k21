from itertools import repeat
from scipy.sparse import coo_matrix
from collections import defaultdict, Counter
from numpy import sign
from tqdm import tqdm

# data = """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2
# """
with open(
    "/Users/akanksha.sunalkar/advent-of-code-2k21/problem_5/pr_5.txt", "r"
) as readfile:
    data = readfile.readlines()
INCLUDE_DIAG = True
# Part1
data_coordinates = []
for line in data:
    if not line:
        continue
    point1, point2 = line.strip().split(" -> ")
    point1 = [int(x) for x in point1.split(",")]
    point2 = [int(x) for x in point2.split(",")]
    if point1[0] == point2[0] or point1[1] == point2[1]:
        data_coordinates.append((point1, point2))
    elif INCLUDE_DIAG:
        data_coordinates.append((point1, point2))

row_coord = []
col_coord = []
for point1, point2 in data_coordinates:
    if point1[0] == point2[0]:
        change_axis = 1
    elif point1[1] == point2[1]:
        change_axis = 0
    else:
        continue
    sorted_points = sorted([point1, point2], key=lambda x: x[change_axis])

    for a1, a2 in zip(
        range(sorted_points[0][change_axis], sorted_points[1][change_axis] + 1),
        repeat(sorted_points[0][~change_axis]),
    ):
        if change_axis == 0:
            row_coord.append(a1)
            col_coord.append(a2)
        else:
            row_coord.append(a2)
            col_coord.append(a1)

coo_no_diag = coo_matrix(
    (list(repeat(1, times=len(row_coord))), (row_coord, col_coord)),
    shape=(max(row_coord) + 1, max(col_coord) + 1),
)
num_positions_no_diag = (coo_no_diag >= 2).count_nonzero()
print(f"Part1 answer: {num_positions_no_diag}")


# Part2
def get_diagonal_points(start_x, start_y, end_x, end_y):
    if start_x > end_x:
        start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y
    slope = (end_y - start_y) // (end_x - start_x)
    for i, j in zip(range(start_x, end_x + 1), range(start_y, end_y + slope, slope)):
        yield i, j


for point1, point2 in data_coordinates:
    if point1[0] == point2[0] or point1[1] == point2[1]:
        continue

    for a1, a2 in get_diagonal_points(point1[0], point1[1], point2[0], point2[1]):
        row_coord.append(a1)
        col_coord.append(a2)

coo_with_diag = coo_matrix(
    (list(repeat(1, times=len(row_coord))), (row_coord, col_coord)),
    shape=(max(row_coord) + 1, max(col_coord) + 1),
)

num_positions_with_diag = (coo_with_diag >= 2).count_nonzero()
print(f"Part2 answer: {num_positions_with_diag}")
