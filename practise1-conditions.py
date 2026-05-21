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
