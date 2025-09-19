# list = ["one", "two", "three"]
# print(list)

# age = 20
# student = True

# print(age>18 and student)
# print(age>25 or student)
# print(student == False)

# x = 10
# x +=5
# print(x)

# a = [1,2,3]
# b = a
# c = [1,2,3]
# print(a is b)

# veg = ['Karela','Aloon','Tamatar']

# print('Aloon' in veg)
# print('potato' not in veg)

# age = 17

# if age > 18:
#     print("can vote")
# elif age < 18:
#     print("can`t vote")
# else:
#     print("error")

# age = int(input('enter your age:'))

# if age >=18 and age <=100:
#     print('you can vote')
    
# elif age >101:
#     print('fake user')

# else:
#     print('enter valid age')


num1 = int(input('number one: '))
num2 = int(input('number two: '))

choice = input('enter your choice: + - * % /: ')

if choice == '+':
    print(f'add:',num1+num2)
elif choice == '-':
    print(f'sub: ',num1-num2)
elif choice == '*':
    print(f'mul: ',num1*num2)
elif choice == '%':
    print('mod: ',num1%num2)
elif choice == '/':
    print(f'div: ',num1/num2)
else:
    
    print('invalid calculation')