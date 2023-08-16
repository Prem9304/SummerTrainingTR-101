def count_ones_zeros(number):
    binary_representation = bin(number)[2:]  
    count_ones = binary_representation.count('1')
    count_zeros = binary_representation.count('0')
    return count_ones, count_zeros


number = int(input("Enter a number: "))

count_ones, count_zeros = count_ones_zeros(number)

print(f"Number of 1s: {count_ones}")
print(f"Number of 0s: {count_zeros}")
