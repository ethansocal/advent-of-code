from pathlib import Path

Puzzle = list


def read_puzzle(file: str) -> Puzzle:
    output = []
    for i in file.splitlines():
        pass

    return output


def part1(puzzle: Puzzle):
    pass


def part2(puzzle: Puzzle):
    pass


if __name__ == '__main__':
    puzzle_file = read_puzzle(open(Path(__file__).parent / ".." / "inputs" / (Path(__file__).stem + ".txt")).read())
    part1(puzzle_file)
    part2(puzzle_file)