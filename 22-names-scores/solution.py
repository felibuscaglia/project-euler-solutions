from pathlib import Path

text = (Path(__file__).parent / "names.txt").read_text()
names = [name.strip('"') for name in text.split(",")]


def merge(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left = merge(left)
    right = merge(right)

    return sort(left, right)

def sort(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    
    sorted = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    if j < len(right):
        sorted.extend(right[j:])
    elif i < len(left):
        sorted.extend(left[i:])
    
    return sorted


sorted = merge(names)

def calculate_score(sorted_names):
    score = 0

    for index, name in enumerate(sorted_names):
        name_score = 0

        for char in name:
            name_score += ord(char) - ord('A') + 1
        
        score += (name_score * (index + 1))
    
    print(f"Total of all the name scores: {score}")

calculate_score(sorted)