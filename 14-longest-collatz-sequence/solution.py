longest = (None, None)
cache = {}

for i in range(1, 1_000_000):
    length = 0
    val = i

    while val != 1:
        cached_sum = cache[val] if val in cache else None

        if cached_sum:
            length += cached_sum
            val = 1
        else:
            val = val / 2 if val % 2 == 0 else (3 * val + 1)
            length += 1
    
    cache[i] = length
    
    if longest[1] is None or length > longest[1]:
        longest = (i, length)

print(f"{longest[0]} is the starting number that produces the longest chain with length {longest[1]}")
