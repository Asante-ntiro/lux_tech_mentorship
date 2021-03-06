import math

#does not consider wrong input e.g. string
n = int(input("Enter number to see if it is in the Fibonacci Sequence "))

#helper function
def isPerfectSquare(x):
    s = math.sqrt(x)
    return s*s == x
#a number is in the fibonacci sequence iff the below values are perfect squares
def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

def showUser(n):
    if isFibonacci(n) == TRUE:
        print("The number you entered IS in the Fibonacci sequence")
    else:
        print("the number you entered IS NOT in the Fibonacci sequence")








