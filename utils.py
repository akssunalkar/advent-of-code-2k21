from pathlib import Path
from typing import Union, List

HOME_DIR = Path("/Users/akanksha.sunalkar/advent-of-code-2k21/")


def open_file(file_path: Path, as_list_values: bool) -> Union[List[str], str]:
    if as_list_values:
        with (HOME_DIR / file_path).open(mode="r") as readfile:
            file_contents = readfile.readlines()
    else:
        with (HOME_DIR / file_path).open(mode="r") as readfile:
            file_contents = readfile.read()
    return file_contents
