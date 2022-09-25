

# Lab task: 01

list1=[]
print("Enter the first list elements")
for i in range(5):
    val = input("Enter values: ")
    n = int(val)
    list1.append(n)

list2=[]
print("Enter the second list elements")
for i in range(5):
    val = input("Enter values: ")
    n = int(val)
    list1.append(n)

list3 = sorted(list1 + list2)
print("Sorted elements are: " +str(list3))


# Lab task: 02

list1=[]
print("Enter the first list elements")
for i in range(5):
    val = input("Enter values: ")
    n = int(val)
    list1.append(n)

list2=[]
print("Enter the second list elements")
for i in range(5):
    val = input("Enter values: ")
    n = int(val)
    list1.append(n)
list3 = list1 + list2
print(list3)
print("Largest no: " +str(max(list3)))
print("Smallest no: " +str(min(list3)))


# Lab task: 03
from math import *         
x= float(input("Enter value of x"))    
h= float(input("Enter value of h"))

m= {sin(x+h) - sin{x} }/h
n= cos(x)
print(m)
print(n)
if(m==n):
    print("Equal")
else:
    print("Not equal")




# Lab task: 04
dict = {("Tooba", "Aftab"): "11-08-2003", ("Hafsa", "Hanif"): "03-03-2002", ("Fatima", "Mehtab"): "05-12-2001"}
print("Welcome to the birthday dictionary. ")
for first, last in dict:
    print(first, last)
name = input("Who's birthday do you want to look up? ")
names = name.split()
search = (names[0].capitalize(), names[1].capitalize())
if search in dict:
    print(name.upper(), " birthday is on ", dict[search])
else:
    print("Record Not Found")



#Lab task: 05

sample_dict = {"name": "Tooba", "age": 20, "salary": 8000, "city": "New york"}
key = ["name", "salary"]
my_dict = {k: sample_dict[k] for k in key}
print(my_dict)    

