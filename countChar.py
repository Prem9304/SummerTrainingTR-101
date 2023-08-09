def count_char_occurrences(input_string, target_char):
    count = 0
    for char in input_string:
        if char == target_char:
            count += 1
    return count

# Input a string and a character to search for
input_string = input("Enter a string: ")
target_char = input("Enter the character to count: ")

if len(target_char) != 1:
    print("Please enter a single character.")
else:
    occurrences = count_char_occurrences(input_string, target_char)
    print(f"The character '{target_char}' appears {occurrences} times in the string.")
