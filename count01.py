def count(num):
    number = str(num)
    count0 = number.count('0')
    count1 = number.count('1')
    print("Number of 0s are:", count0)
    print("Number of 1s are:", count1)

number = int(input("Enter a number: "))
count(number)
