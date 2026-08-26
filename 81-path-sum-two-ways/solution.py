from functools import cache
from pathlib import Path

text = (Path(__file__).parent / "matrix.txt").read_text().strip()
cells = [[int(n) for n in row.split(",")] for row in text.splitlines()]

rows = len(cells)
cols = len(cells[0])


def forced_path_sum(row, col):
    total = 0

    if row == rows - 1:
        for c in range(col, cols):
            total += cells[row][c]
        return total

    if col == cols - 1:
        for r in range(row, rows):
            total += cells[r][col]
        return total

    return total


@cache
def min_path_sum(row=0, col=0):
    if row == rows - 1 and col == cols - 1:
        return cells[row][col]

    if row == rows - 1 or col == cols - 1:
        return forced_path_sum(row, col)

    return cells[row][col] + min(
        min_path_sum(row, col + 1),
        min_path_sum(row + 1, col),
    )


print(min_path_sum())
