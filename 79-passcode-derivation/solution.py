from pathlib import Path

keylog = (Path(__file__).parent / "keylog.txt").read_text().strip()
attempts = [attempt for attempt in keylog.splitlines()]

class Node:
    def __init__(self, value: str) -> None:
        self.value = value
        self.deps = []
    
    def add_dep(self, dep: "Node") -> None:
        self.deps.append(dep)

nodes = {}

for attempt in attempts:
    for index, num in enumerate(attempt):
        prereq = attempt[index - 1] if index - 1 > -1 else None

        if num not in nodes:
            nodes[num] = Node(value=num)

        if prereq is not None:
            if prereq not in nodes:
                nodes[prereq] = Node(value=prereq)

            nodes[num].add_dep(nodes[prereq])

visiting = set()
visited = set()
order = []

def dfs(node: "Node"):

    if node.value in visiting:
        return False
    
    if node.value in visited:
        return True
    
    visiting.add(node.value)

    for dep in node.deps:
        if not dfs(dep):
            return False
    
    visiting.remove(node.value)
    visited.add(node.value)
    order.append(node.value)

    return True
    
for node in nodes.values():
    if not dfs(node):
        break
else:
    print("".join(order))

