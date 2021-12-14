from collections import defaultdict
import math
from utils import open_file
from pathlib import Path

data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

template_data = open_file(file_path=Path("problem_14/pr_14.txt"), as_list_values=True)
pattern_map = {}
for i, line in enumerate(template_data):
    if i == 0:
        TEMPLATE = line.strip()
    if not line.strip():
        continue
    if "->" in line:
        pair, letter = line.strip().split(" -> ")
        pattern_map[pair] = letter


pattern_to_pattern_map = defaultdict(list)
for pattern, letter in pattern_map.items():
    new_pattern_1, new_pattern_2 = pattern[0] + letter, letter + pattern[1]
    if new_pattern_1 in pattern_map:
        pattern_to_pattern_map[pattern].append(new_pattern_1)
    if new_pattern_2 in pattern_map:
        pattern_to_pattern_map[pattern].append(new_pattern_2)

step = 1
template_patterns = ["".join([l1, l2]) for l1, l2 in zip(TEMPLATE, TEMPLATE[1:])]
print(TEMPLATE, template_patterns)
temp = {p: 1 for p in template_patterns}
while step < 41:
    new_temp = defaultdict(int)
    for pattern, count in temp.items():
        pattern_list = pattern_to_pattern_map[pattern]
        for p in pattern_list:
            new_temp[p] += count
    temp = new_temp.copy()
    step += 1

letter_counter = defaultdict(int)
for p, count in new_temp.items():
    letter_counter[p[0]] += count
    letter_counter[p[1]] += count

final_counter = {k: math.ceil(v / 2) for k, v in letter_counter.items()}
print(final_counter)
final_answer = max(final_counter.values()) - min(final_counter.values())
print(final_answer)
