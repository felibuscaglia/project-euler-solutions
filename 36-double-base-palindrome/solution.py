def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def is_binary_palindrome(n):
    binary = bin(n)[2:]

    return binary == binary[::-1]

total_sum = 0

for i in range(1, 1_000_001):
    if is_palindrome(i) and is_binary_palindrome(i):
        total_sum += i
    
print(f'Total sum: {total_sum}')