def divide(a, b):
    if b == 0:
        return None
    return a / b

numbers = [10, 20, 30]

for i in range(len(numbers)):
    print(numbers[i])

print(divide(10, 0))