def check_prime(num):
    if num < 2:
        print("Number is not prime")
        return

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Number is not prime")
            return

    print("Number is prime")

num = int(input("Enter a number: "))
check_prime(num)
