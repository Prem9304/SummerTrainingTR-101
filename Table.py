def print_table(num, current):
    if current > 10:
        return
    print(f"{num} * {current} =", num * current)
    print_table(num, current + 1)

num = int(input("Enter The number: "))
print_table(num, 0)  # Start with current = 0
