def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
num=input("enter the number")
n=int(num)
f=factorial(n)
print("Factorial is",f)
