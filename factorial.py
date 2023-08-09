# 12.	Python Program to find factorial of a number using recursion.
def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num-1)

number = int(input("Enter Number to find Factorial:"))
factrial = fact(number)
print("Factorial is", factrial)
