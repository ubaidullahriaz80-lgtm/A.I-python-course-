name = "ubaidullah"
age = 22
country = "pakistan"
city = "multan"
print(f'my name is,{name},{type(name)}')
print('my age is',age,type(age))
print('my country is',country,type(country))
print('my city is',city,type(city))

integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

print("Value:",new_number)
print("Data Type:",type(new_number))

string_num = '12'
int_num = 25
print('data type of string before type casting',type(string_num))
string_num = int(string_num)
print('data type of string after type casting', type (string_num))
sum = int_num + string_num
print (sum,type(sum))