str0 = "Introducing to My Family"
str1 = "Md.Asikur Rahman"
str2 = "Md.Abdur Rahman"
str3 = "Ayesha Akter"
str4 = "Fatema Akter"
print(str0)
print("My name is", str1)
print("My father's name is", str2)
print("My mother's name is", str3)
print("My sister's name is", str4)

#working with string
strA = "Apna "
strB = "College"
strC = strA + strB
print(strC)
print (strA + strB)
print(strA+" "+strB)

#length of string in python
strA = "Apna College"
print("Length of strA is", len(strA))

#indexing in python
strA = "Apna College"
print("strA[0] is", strA[0])
print("strA[1] is", strA[1])
print("strA[2] is", strA[2])
print("strA[3] is", strA[3])
print("strA[4] is", strA[4])
print("strA[5] is", strA[5])
print("strA[6] is", strA[6])
print("strA[7] is", strA[7])
print("strA[8] is", strA[8])
print("strA[9] is", strA[9])
print("strA[10] is", strA[10])
print("strA[11] is", strA[11])

strC = "Amar Sonar Bangla"
ch= strC[0]
print("ch is", ch)
print(strC[8:14]) #slicing in python
# strC[5] = "k" #strings are immutable in python, so this will give an error
print(strC[5:len(strC)]) #slicing from index 5 to the end of the string
print(strC[:5]) #slicing from the beginning of the string to index 4

#listing in python
Student = ["Asikur", "95.5","A"] # in list we can store different types of data such as string, float and char
print(Student)
print(len(Student))
print(type(Student))
print(Student[0])
print(Student[1])

Student[0] = "Rahman" # we can change the value of a list element
print(Student)

#list slicing in python
print(Student[1:4]) #slicing from index 1 to index 3
print(Student[:2]) #slicing from the beginning of the list to index 1
print(Student[2:]) #slicing from index 2 to the end of the list
print(Student[-1]) #slicing from the end of the list to index -1
print(Student[-3:-1]) #slicing from index -3 to index -2




