result = 600851475143

for i in range(2, result):
    if result == 1:
        break
    elif result % i == 0:
        result /= i
        highest = i
        continue

print(highest)
