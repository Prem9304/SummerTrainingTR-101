def get_largest_number(lst):
    if not lst:
        return None
    
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

def search_elements(lst, element):
    indices = [i for i, num in enumerate(lst) if num == element]
    return indices

# Input the elements into a list
numbers = []
num_count = int(input("Enter the number of elements: "))

for i in range(1, num_count + 1):
    while True:
        try:
            num = int(input(f"Enter the {i}{'st' if i == 1 else 'nd' if i == 2 else 'th'} number: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Get largest number from the list
largest_number = get_largest_number(numbers)
print("Largest number in the list:", largest_number)

# Search for an element in the list
while True:
    try:
        search_value = int(input("Enter a value to search: "))
        found_indices = search_elements(numbers, search_value)
        if found_indices:
            locations = ', '.join(str(idx + 1) + ('st' if idx == 0 else 'nd' if idx == 1 else 'rd' if idx == 2 else 'th') for idx in found_indices)
            print(f"{search_value} is present at {locations} location(s) in the list.")
        else:
            print(f"{search_value} is not present in the list.")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
