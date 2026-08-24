longest = (0, 0)

for i in range(2, 1000):
    remainder = 10 % i
    remainders = {1, remainder}
    digits = []

    while remainder != 0:
        print (f"Remainder: {remainder} for i {i}")
        digits.append((remainder * 10) / i)
        remainder = (remainder * 10) % i

        if remainder in remainders:
            break
        else:
            remainders.add(remainder)
    
    if len(digits) > longest[1]:
        longest = (i, len(digits))

print(f"Longest index {longest[0]} with length {longest[1]}")