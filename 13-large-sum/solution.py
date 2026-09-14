from pathlib import Path

text = (Path(__file__).parent / "numbers.txt").read_text()
numbers = [name.strip('"') for name in text.split("\n")]

acc = list(map(int, numbers[0]))

for num in numbers[1:]:
    current = list(map(int, num))

    acc_index = len(acc) - 1
    current_index = len(current) - 1
    carry = 0

    while current_index >= 0 or carry:
        if acc_index < 0:
            acc.insert(0, carry)
            break

        digit = current[current_index] if current_index >= 0 else 0

        curr_sum = acc[acc_index] + digit + carry

        acc[acc_index] = curr_sum % 10
        carry = curr_sum // 10

        acc_index -= 1
        current_index -= 1

print(f'First ten digits: {"".join(map(str, acc[:10]))}')
print(f'Complete: {"".join(map(str, acc))}')