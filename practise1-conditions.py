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