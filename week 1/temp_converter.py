Fahrenheit  = float(input('enter the temp in Fahrenheit: '))
celsius = (Fahrenheit  -32 )*5/9
print('celsius',celsius)
if celsius < 10:
    print('wether is cold')
elif celsius > 25:
    print('wether is hot')
elif celsius > 40:
    print('wether is very hot')