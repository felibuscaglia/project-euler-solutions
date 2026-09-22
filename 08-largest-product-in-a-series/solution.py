from pathlib import Path
import math

series = (Path(__file__).parent / "series.txt").read_text().strip()

curr_prod = math.prod(int(num) for num in series[0:13])
greatest = curr_prod

for i in range(13, len(series)):
    curr_el = int(series[i])
    el_to_remove = int(series[i - 13])

    if el_to_remove == 0:
        # I could've counted the zeroes so that I don't need to recompute here, but I'm not aiming for performance.
        curr_prod = math.prod(int(num) for num in series[i - 12:i + 1])
    else:
        curr_prod = int(curr_prod / el_to_remove)
        curr_prod = curr_prod * curr_el

    if curr_prod > greatest:
        greatest = curr_prod

print(f"Greatest product: {greatest}")
    