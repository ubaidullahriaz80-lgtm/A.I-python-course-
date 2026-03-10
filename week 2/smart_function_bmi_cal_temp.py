def cal():
    num_1 = float(input('enter the First number :'))
    oper = input('enter a operator (+,-,*,/,//,%,**,<,>,==) :')
    num_2 = float(input('enter the Second number :'))
    if oper == '+':
       print(num_1 + num_2)
    elif oper == '-':
         print(num_1 - num_2)
    elif oper == '*':
         print(num_1 * num_2)
    elif oper == '/':
         print(num_1 / num_2)
    elif oper == '//':
         print(num_1 // num_2)
    elif oper == '%':
         print(num_1 % num_2)
    elif oper == '**':
         print(num_1 ** num_2)
    elif oper == '<':
         print(num_1 < num_2)
    elif oper == '>':
         print(num_1 > num_2)
    elif oper == '==':
         print(num_1 == num_2)
    else:
         print('invalid operator')

def bmi():
    weight = float(input("Enter your weight in kilograms: "))
    height  = float(input("Enter your height in feet: "))
    height = height * 0.3048

    bmi = weight / (height ** 2)

    print("Your BMI is:",bmi)

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 24.9:
        print("Category: Normal weight")
    elif bmi < 29.9:
        print("Category: Overweight")
    else:
        print("Category: Obese")
def temp():

    Fahrenheit  = float(input('enter the temp in Fahrenheit: '))
    celsius = (Fahrenheit  -32 )*5/9
    print('celsius',celsius)
    if celsius < 10:
       print('wether is cold')
    elif celsius > 25:
        print('wether is hot')
    elif celsius > 40:
         print('wether is very hot')
print('press 1 for cal')
print('press 2 for bmi')
print('press 3 for temp')
choice = input('enter your choice')
if choice == '1':
   cal()
elif choice == '2':
    bmi()
elif choice == '3':
     temp()

