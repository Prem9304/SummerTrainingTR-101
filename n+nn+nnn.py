def compute(n):
    print("Result after computing n + n*n + n*n*n is:", n + n*n + n*n*n)
    print("Result after computing n + nn + nnn is:", n + (n*10)+n + (n*100)+(n*10)+n)

n = int(input("Enter the number: "))
compute(n)
