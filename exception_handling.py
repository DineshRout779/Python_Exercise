a = input("enter first number\n")
b = input("enter second number\n")
a = int(a)
b = int(b)
try:
    result = a/b
    result = str(result)
    print("Result = "+result)
except ZeroDivisionError:
    print("b can not be zero, try again.")
