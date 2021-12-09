from pathlib import Path
from utils import open_file
from collections import Counter
import numpy as np

output_values = []
signals = []

signals_and_output = open_file(
    file_path=Path("problem_8/pr_8.txt"), as_list_values=True
)
for line in signals_and_output:
    line = line.split(" | ")
    output_values.append(line[1].strip().split())
    signals.append(line[0].strip().split())

# output_values = [output.split(" | ")[1].strip().split() for output in signals_and_output]
length_digit_map = {2: "1", 4: "4", 3: "7", 7: "8"}
counter = Counter()
for i, value_list in enumerate(output_values):
    length_value = [len(val) for val in value_list if len(val) in length_digit_map]
    counter.update(Counter(length_value))

print(counter, len(output_values))
# Part 2
total = 0
for signal, output_val in zip(signals, output_values):
    found = {}
    for pattern in signal:
        if len(pattern) == 2:
            found[1] = set(pattern)
        elif len(pattern) == 3:
            found[7] = set(pattern)
        elif len(pattern) == 4:
            found[4] = set(pattern)
        elif len(pattern) == 7:
            found[8] = set(pattern)

    segments = {"top": found[7] - found[4]}
    rights = found[4] & found[1]
    for pattern in signal:
        if len(pattern) == 5 and all(right in pattern for right in rights):
            found[3] = set(pattern)
            break

    segments["top_left"] = found[4] - found[3]
    segments["middle"] = found[4] - rights & found[3]
    segments["bottom"] = (
        found[3] - rights - segments["middle"] - segments["top_left"] - segments["top"]
    )
    found[0] = found[8] - segments["middle"]

    segments["bottom_left"] = (
        found[0] - segments["top"] - segments["bottom"] - rights - segments["top_left"]
    )
    for pattern in signal:
        if len(pattern) == 5 and all(
            list(segments[key])[0] in pattern
            for key in ("top", "top_left", "middle", "bottom")
        ):
            found[5] = set(pattern)
            break

    for pattern in signal:
        if len(pattern) == 5 and all(found[key] != set(pattern) for key in (3, 5)):
            found[2] = set(pattern)
            break

    segments["top_right"] = (
        found[2]
        - segments["top"]
        - segments["middle"]
        - segments["bottom_left"]
        - segments["bottom"]
    )
    segments["bottom_right"] = rights - segments["top_right"]
    found[6] = found[8] - segments["top_right"]
    found[9] = found[8] - segments["bottom_left"]

    total += int(
        "".join(
            map(
                str,
                [
                    next(
                        int(key)
                        for key, value in found.items()
                        if value == set(pattern)
                    )
                    for pattern in output_val
                ],
            )
        )
    )

print(total)
