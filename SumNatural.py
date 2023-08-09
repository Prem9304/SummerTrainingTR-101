def sumNatural(limit):
    total_sum = limit * (limit + 1) // 2
    return total_sum

limit = int(input("Enter a Limit for the sum of natural numbers: "))
result = sumNatural(limit)
print(result)
