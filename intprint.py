#aren’t divisible by either 2 or 3 and lie between 1 and 50 in Python.

for num in range(1, 51):
    if num % 2 != 0 and num % 3 != 0:
        print(num)
