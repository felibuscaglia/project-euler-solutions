total_sum = 0
squares_sum = 0

for n in range(0, 101):
    total_sum += n
    squares_sum += n ** 2

total_sum_squared = total_sum ** 2
print(f"Difference: {total_sum_squared - squares_sum}")