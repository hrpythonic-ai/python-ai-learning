#Array: an array is a collection of items stored in a single variable, where each item can be executed by its position.
#-------------------------------
#-------------------------------
#making 1000 variables for user
name1='hassan raza'
name2='ahmad raza'
name3='mehboob raza'
name4='arslan'
name5='khuram'

#Memory fails
#1000 variables not managed
#-------------------------------
#-------------------------------
names=['ali','john','doe',1,2,3,4,True,False]
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])
#-------------------------------
#-------------------------------
#pushing data to array:
names.append('arslan')
print(names)
#-------------------------------
#-------------------------------
#by inserting at a specific index
names.insert(1,'muzamil')
print(names)
#-------------------------------
#-------------------------------
#removing data to array:
names.remove("ali")
print(names)
#-------------------------------
#-------------------------------
#remove element at specific index:
names.pop(2)
print(names)
#-------------------------------
#-------------------------------
#Get index of element
print(names.index('arslan'))
#-------------------------------
#-------------------------------
#How many elements present in an array:
print(len(names))
#-------------------------------
#-------------------------------
#Take five names from user using loop and append it in array:
#and afterwards print the elements in an array:
"""
names=[]
for i in range(5):
    name=input("Enter the name: ")
    names.append(name)
print(names)
"""
#-------------------------------
#-------------------------------
#How many times an element is present in an array:
nums=[4,3,5,5,6,9,7,6,5,5,5,4,3,2,2,100,34,34,4,4,6,5,5,]
print(nums.count(5))
#-------------------------------
#-------------------------------
#Reverse an array:
names=['ali','hassan','ahmad','khurram','noor','mubeen']
names.reverse()
print(names)
#-------------------------------
#-------------------------------
#How to check which are students and which are job_holders
students=['hassan raza','muzamil mehmood','arslan arif','khurram','ahamd']
job_holders=['gulraiz','daler','talal','rubab','qaiser','tayyaba']

#ask user his/her name
user_name=input("Enter your name: ")
if user_name in students:
    print("Yes user is in students.")
elif user_name in job_holders:
    print("Yes user name is in job_holders.")
else:
    print("user is not found in any list")

#-------------------------------
#-------------------------------
#find largest number in an array:
#find smallest number in an array:
age=[21,76,98,34,55,78,33]
max_age=max(age)
print(max_age)
min_age=min(age)
print(min_age)
#-------------------------------
#-------------------------------
