import math

n = int(input("Enter number to see if it is in the Fibonacci Sequence "))

def isPerfectSquare(x):
    s = math.sqrt(x)
    return s*s == x

def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

def showUser(n):
    if isFibonacci(n) == TRUE:
        print("The number you entered IS in the Fibonacci sequence")
    else:
        print("the number you entered IS NOT in the Fibonacci sequence")








