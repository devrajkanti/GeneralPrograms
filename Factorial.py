def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

number = int(input("Enter the number "))
if number < 0:
    print("Factorial does not exist for negative number")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of ", number, "is ", factorial(number))
