numbers: list[int] = list(range(1_000))

for i in range(500):
    if not bool(numbers[i] % 2):
        del numbers[i]
    else:
        numbers[i]= numbers[i] * i

print(numbers)
