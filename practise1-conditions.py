#Traffic light code
Light = input("light =")
if(Light == "red"):
    print("Stop")
elif(Light == "yellow"):
    print("look")
elif(Light == "green"):
    print("go")
else:
    print("Light is broken")

#Grades of students code
marks =int(input("marks ="))

if( marks >= 90):
       print("A")
elif( marks >= 80 and marks < 90):
    print("B")
elif( marks >= 70 and marks < 80):
    print("C")
else:
    print("D")

    #Arithmetic operations code
a = int(input("x ="))
b = int(input("y ="))
c = a + b
print("Sum =", c)   
c = a - b
print("Difference =", c)
c = a * b
print("Product =", c)
c = a / b
print("Quotient =", c)
c = a % b
print("Remainder =", c)
c = a ** b
print("Power =", c)


#relational operators code
a = int(input("x ="))
b = int(input("y ="))

print("x > y is", a > b)
print("x < y is", a < b)
print("x >= y is", a >= b)
print("x <= y is", a <= b)
print("x == y is", a == b)
print("x != y is", a != b)

#assignment operators code
num = int(input("num ="))
num += 5
num -= 3
num *= 2
num /= 4
num %= 3
num **= 2
print("num =", num)
#type casting code
a = "10" #a is a string
b = int(a) #b is an integer
c = 5
d = b + c
print("d =", d)

#Variable and data types code
name = input("name =")
age = int(input("age ="))
marks = float(input("marks ="))
 
print("Name:", name)
print("Age:", age)
print("Marks:", marks)

#wap to input a side of a square and print its area
a = float(input("side of square ="))
area = a * a
print("Area of square =", area)
#wap to input 2 floating point numbers and print their average a
A = float(input("num1 ="))
B = float(input("num2 ="))
average = (A + B) / 2
print("Average =", average)
 
#condition
a = int(input("num1 ="))
b = int(input("num2 ="))

if(a>=b):
    print("True")
else: 
    print("False")
