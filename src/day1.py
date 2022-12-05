from pathlib import Path
from typing import List

Puzzle = List[List[int]]


def read_puzzle(contents: str) -> Puzzle:
    output = [[]]
    for i in contents.splitlines():
        if i == "":
            output.append([])
        else:
            output[-1].append(int(i))

    return output


def day1(puzzle: Puzzle):
    print(max([sum(i) for i in puzzle]))


def day2(puzzle: Puzzle):
    thing = [sum(i) for i in puzzle]
    thing.sort(reverse=True)
    print(sum(thing[0:3]))


if __name__ == "__main__":
    puzzle_file = read_puzzle(open(Path(__file__).parent / ".." / "inputs" / (Path(__file__).stem + ".txt")).read())
    day1(puzzle_file)
    day2(puzzle_file)
