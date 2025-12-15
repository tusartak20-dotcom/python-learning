#Code to print Name after taking it as input
name = input("Enter Your Name?")
greetings="Hello "+ name+ ', Welcome to the Python Programming'
print(greetings)

#code to print a square box with *
print("* * * ")
print("")
print(" ")
print("")
print(" ")
print("")
print(" * * *")

print('Hello,\'Tusar\' World!')
print(type("Hello"))
print(type(True))
print(type(type(True))) # <class 'type'>
print(type(-1234))
print(type(1234.0))
print(type('a'))
#Integer
age = 26
print('Age: ', age)

#float
height = 1.87
print("Height: ", height, "metres")

# string
name='John'
print("Name: "+ name) # + only works with string for concat otherwise use ,
#print(number) NameError


# Variables in python
name = "John"  # String variable
age = 20  # Integer variable
gpa = 3.9  # Float variable
is_student = True
  # Boolean variable

# Prints all the data in string format
print("Name: " + name)
print("Age: " + str(age))
print("GPA: " + str(gpa))
print("Is student: " + str(is_student))

print(11//-5) #-3
print (-11 // 5) # -3
print(11//5) # 2
print( 11 % -5) # 11 - (11 // -5) * -5 = -4
print(-11 % 5) # -11 - (-11 // 5) * 5 = 4
print(4**2) # 16
print(31**331%20)

x = 10
y = 20
sum_result = x + y
diff_result = x - y
mul_result = x * y
div_result = x / y
output = "Sum: {}, Difference: {}, Multiplication: {}, Division: {}".format(sum_result, diff_result, mul_result, div_result)
print(output)


a = int(input())
b = int(input())
c = int(input())
print(b * a - c)

print(int(2 ** 179))