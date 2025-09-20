# try:
#     num = int(input("enter numbe: "))
#     result = 10 / num
#     print(f"result: {result}")
# except ZeroDivisionError:
#     print("You can not divide with 0")

try:
    num1 = int(input("enter number one: "))
    num2 = int(input("enter number two: "))

    try:
        result = num1 / num2
        print(f"Result:{result}")
    except ZeroDivisionError:
        print("You cant divide with zero")
except ValueError:
    print("you must provide a valid input")




