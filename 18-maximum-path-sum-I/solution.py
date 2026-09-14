from pathlib import Path

text = (Path(__file__).parent / "triangle.txt").read_text().strip()
inverted_triangle_rows = [
    [int(n) for n in row.split(" ")] for row in text.splitlines()
][::-1]

def get(arr, index):
    return arr[index] if index < len(arr) else None

class Node:
    def __init__(self, val: int, left, right) -> None:
        self.value = val
        self.left = left
        self.right = right

prev_edges = []

for row in inverted_triangle_rows:
    curr_edges = []

    for index, val in enumerate(row):
        left = get(prev_edges, index)
        right = get(prev_edges, index + 1)

        node_val = val

        if left is not None and right is not None:
            node_val += max(left.value, right.value)
        
        curr_edges.append(Node(val=node_val, left=left, right=right))
    
    prev_edges = curr_edges


root = prev_edges[0]

print(f"Maximum path sum: {root.value}")

        