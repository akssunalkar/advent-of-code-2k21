from pathlib import Path
from utils import open_file
from collections import defaultdict

# data="""start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end"""


data = open_file(file_path=Path("problem_12/pr_12.txt"), as_list_values=True)

all_connections = defaultdict(list)
for c in data:
    p1, p2 = c.strip().split("-")
    all_connections[p1].append(p2)
    if p1 != "start" and p2 != "end":
        all_connections[p2].append(p1)
print(all_connections)


def traverse(cave_map, visited, loc, visited_small, allow_visited_small: bool):
    new_visited = visited.copy()
    if loc == "end":
        return 1
    if loc in new_visited:
        new_visited[loc] += 1
    else:
        new_visited[loc] = 1

    paths = 0
    for to in cave_map[loc]:
        if to.isupper():
            paths += traverse(
                cave_map, new_visited, to, visited_small, allow_visited_small
            )
        elif to not in new_visited:
            paths += traverse(
                cave_map, new_visited, to, visited_small, allow_visited_small
            )

        elif (
            to in new_visited
            and new_visited[to] < 2
            and not visited_small
            and allow_visited_small
        ):
            paths += traverse(cave_map, new_visited, to, True, allow_visited_small)

    return paths


visited = {}
# Part 1
all_paths = traverse(
    cave_map=all_connections,
    visited=visited,
    loc="start",
    visited_small=False,
    allow_visited_small=False,
)
print(all_paths)
# #part2
all_paths = traverse(
    cave_map=all_connections,
    visited=visited,
    loc="start",
    visited_small=False,
    allow_visited_small=True,
)
print(all_paths)
