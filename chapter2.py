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

Name = [1,2,3]
Name.append(4) # we can add an element to the end of the list using append() method
Name.sort()
Name.reverse() # we can reverse the order of the list using reverse() method
Name.insert(1,3)
Name.remove(2) # we can remove an element from the list using remove() method
Name.sort(reverse=True) # we can sort the list in descending order using sort() method with reverse=True
Name.pop() # we can remove the last element from the list using pop() method

#tuple in python
Val = (87,64,35,95,76) # in tuple we can store different types of data such as int, float and char
#Val =[0] = 90 # we cannot change the value of a tuple element because tuples are immutable in python
tup1 = ()
tup2 = (1,)
tup3 = (1,2,3)
#Val.index(1)
Val.count(1)

#How to check palindrome in python
list1 = ["m", "a","a","m"]
copy_list = list1.copy()
copy_list.reverse()
if(copy_list == list1):
    print("palindrome")
else:
    print("not palindrome")

#Dictionary in python
student = {
    "name" : "Md.Asikur Rahman",
    "subject" : {
        "physics" : 95,
        "chemistry" : 90,
        "math" : 98
    }
    }
#nested dictionary in python
print(student["subject"]["physics"]) # we can access the value of a nested dictionary using the key of the outer dictionary and the key of the inner dictionary
print(student.keys()) # we can get the keys of a dictionary using keys() method
print(list(student.keys()))
print(student.values())
print(list(student.values()))

print(student.items()) # we can get the key-value pairs of a dictionary using items() method
print(list(student.items()))
#print(student["name2"]) # this will give an error because there is no key named "name2" in the dictionary
#print(student.get("name2")) # this will return None because there is no key named "name2" in the dictionary
#student.update({"city" : "Dhaka"}) # we can add a new key-value pair to the dictionary using update() method
new_dict = {"city" : "Dhaka"}
student.update(new_dict)
#name1 = {"name" : "Md.Abdur Rahman"} # this will 

#set in python
collection = {1,2,3,4,5} # in set we can store different types of data such as int, float and char
print(collection)
print(type(collection))
collection.add(6) # we can add an element to a set using add() method
collection.remove(3) # we can remove an element from a set using remove() method
#set in unordered in python
colection2 = {5,5,5,4,4,3,2,2,2,2,1,"world","world","hello","hello"}
print(len(colection2)) # we can see that the length of the set is 6 because it only stores unique elements

