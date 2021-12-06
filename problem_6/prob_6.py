from utils import open_file
from pathlib import Path
from collections import defaultdict

# data="3,4,3,1,2"

data = open_file(file_path=Path("problem_6/pr_6.txt"), as_list_values=True)
fish_numbers = [int(x) for x in data[0].split(",")]

age_map = {8: 7, 7: 6, 6: 5, 5: 4, 4: 3, 3: 2, 2: 1, 1: 0, 0: 6}
fish_count_map = defaultdict(int)
for i in fish_numbers:
    fish_count_map[i] += 1

for i in range(256):
    new_counter = defaultdict(int)
    for num, count in fish_count_map.items():
        new_counter[age_map[num]] += count
        if num == 0:
            new_counter[8] += count
    fish_count_map = new_counter
print(fish_count_map, sum(fish_count_map.values()))
