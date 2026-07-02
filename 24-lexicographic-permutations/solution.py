from itertools import permutations

digits = "0123456789"

millionth_lexicographic_permutation = None

for index, permutation in enumerate(permutations(digits)):
    if index == 999_999:
        millionth_lexicographic_permutation = permutation
        break

print(
    f"The millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 is {"".join(millionth_lexicographic_permutation)}"
)
