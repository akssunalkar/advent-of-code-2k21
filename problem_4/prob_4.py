# Data Formatting
import numpy as np

data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
8  2 23  4 24
21  9 14 16  7
6 10  3 18  5
1 12 20 15 19

3 15  0  2 22
9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
2  0 12  3  7
"""

# split_data = data.split("\n")
with open(
    "/Users/akanksha.sunalkar/advent-of-code-2k21/problem_4/pr_4.txt", "r"
) as readfile:
    split_data = readfile.readlines()

sampled_numbers = split_data[0].split(",")
boards = []
board_num_rows = 5
idx = 1
while True:
    if not split_data[idx].strip():
        idx += 1
    else:
        b = split_data[idx : idx + board_num_rows]
        b_list = [row.split() for row in b]
        boards.append(np.array(b_list))
        idx = idx + board_num_rows

    if idx >= (len(split_data)):
        break


def check_bingo(binary_array):
    row_check = np.any(np.all(binary_array, axis=0))
    column_check = np.any(np.all(binary_array, axis=1))
    return row_check or column_check


def find_bingo_board(bingo_boards, sample_numbers, if_first_winner: bool):
    idx = 0
    bingo = {}
    while True:
        test_set = sample_numbers[0:idx]
        for b_i, b in enumerate(bingo_boards):
            mask = np.isin(element=b, test_elements=test_set)
            if check_bingo(mask) and b_i not in bingo:
                bingo.update({b_i: idx})
        if if_first_winner and len(bingo) == 1:
            break
        if len(bingo) == len(bingo_boards):
            break
        idx += 1
    return bingo


# Part1
board_idx_map = find_bingo_board(
    bingo_boards=boards, sample_numbers=sampled_numbers, if_first_winner=True
)
winner_board_idx = list(board_idx_map.keys())[0]
idx_at_win = board_idx_map[winner_board_idx]
elements_not_found_mask = np.isin(
    element=boards[winner_board_idx],
    test_elements=sampled_numbers[:idx_at_win],
    invert=True,
)
elements_not_found = [
    int(ele) for ele in boards[winner_board_idx][elements_not_found_mask]
]
score = sum(elements_not_found) * int(sampled_numbers[idx_at_win - 1])
print(score)

# Part2
board_idx_map = find_bingo_board(
    bingo_boards=boards, sample_numbers=sampled_numbers, if_first_winner=False
)
loser_board_idx = list(board_idx_map.keys())[-1]
idx_at_last = board_idx_map[loser_board_idx]
elements_not_found_mask = np.isin(
    element=boards[loser_board_idx],
    test_elements=sampled_numbers[:idx_at_last],
    invert=True,
)
elements_not_found = [
    int(ele) for ele in boards[loser_board_idx][elements_not_found_mask]
]
lose_score = sum(elements_not_found) * int(sampled_numbers[idx_at_last - 1])
print(lose_score)
