

# Activity: 01

myList1=[]
print("Enter objects of first list..")
for i in range(5):
    val = input("Enter a value..")
    n = int(val)
    myList1.append(n)

myList2=[]
print("Enter objects of second list..")
for i in range(5):
    val = input("Enter a value..")
    n = int(val)
    myList2.append(n)

list3 =myList1 + myList2
print(list3)


# Activity: 02

def isPalindrome(word):
    temp = word[::-1]
    if temp.capitalize() == word.capitalize():
        return True
    else:
        return False

print(isPalindrome("deed"))    


# Activity: 03
a =[[1,0,0],[0,1,0],[0,0,1]]
b=[[1,2,3],[4,5,6],[7,8,9,]]
c=[]
for indrow in range(3):
    c.append([])
    for indcol in range(3):
      c[indrow].append (0)
      for indaux in range(3):
          c[indrow][indcol] += a[indrow][indaux] * b[indcol][indaux]
print(c)          


#Activity: 04

def perimeter(listing):
              leng = len(listing)
              perimeter=0;
              for i in range(0,leng-1):
                dist = (((listing[i][0] - listing[i+1][0])**2) +((listing[i][1] - listing[i+1][1])**2))**0.5
                
                perimeter = perimeter + dist
              perimeter = perimeter + (((listing[0][0] - listing[leng-1][0])**2)+((listing[0][1] - listing[leng-1][1])**2))**0.5
                               
              return perimeter
    
L = [(1,3) ,(2,7) , (3,9) ,(-1,8)]
print(perimeter(L))


# Activity: 05

def symmDiff(a,b):
    e= set()
    for i in a:
        if i not in b:
            e.add(i)
    for i in b:
        if i not in a:
            e.add(i)
    return e

set1 = {0,1,2,4,5}
set2 = {4,5,7,8,9}
print(symmDiff(set1, set2))

print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))
print(set1^set2)
print(set2^set1)


# Activity: 06
sample={("shoaib","ali"):"02467568877", ("aib" , "li"):"086567875", ("sib" , "ai"):"96578676656",}
firstName = input("Enter first name: ")
lastName = input("Enter last name: ")

searchTuple = (firstName, lastName)
if searchTuple in sample:
    print(sample[searchTuple])
else:
    print("Name not found")


