largest_palindrome_product = None

for i in range (100, 1000):
    for j in range(i, 1000):
        num = i * j
        if str(num) == str(num)[::-1]:
            largest_palindrome_product = max(largest_palindrome_product, num) if largest_palindrome_product is not None else num

print(f"The largest palindrome product is: {largest_palindrome_product}")