from utils import open_file
from pathlib import Path
import numpy as np

# data="""[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]
# """
data = open_file(file_path=Path("problem_10/pr_10.txt"), as_list_values=True)
character_map = {"]": "[", ")": "(", "}": "{", ">": "<"}
illegal_char_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
completion_char_points = {")": 1, "]": 2, "}": 3, ">": 4}
pattern_lines = [line.strip() for line in data]
print(len(pattern_lines))


total_points_corrupt = 0
corrupt_lines_idx = set()
for i, pattern in enumerate(pattern_lines):
    queue = []
    for sp_char in pattern:
        if sp_char in character_map.values():
            queue.append(sp_char)
        if sp_char in character_map:
            if queue.pop() != character_map[sp_char]:
                total_points_corrupt += illegal_char_points[sp_char]
                corrupt_lines_idx.add(i)
##Part 1
print(total_points_corrupt)

##Part 2
pattern_lines = [p for i, p in enumerate(pattern_lines) if i not in corrupt_lines_idx]


reverse_map = {v: k for k, v in character_map.items()}

all_scores = []
for pattern in pattern_lines:
    queue_new = []
    for sp_char in pattern:
        if sp_char in reverse_map:
            queue_new.append(sp_char)
        if sp_char in character_map:
            assert queue_new.pop() == character_map[sp_char]
    score = 0
    for rem_char in queue_new[::-1]:
        score *= 5
        score += completion_char_points[reverse_map[rem_char]]

    all_scores.append(score)
all_scores = sorted(all_scores)
print(f" Middle score: {all_scores[int(len(all_scores)/2)]}")
