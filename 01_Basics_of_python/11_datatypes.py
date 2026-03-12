#___________(DATA TYPES IN PYTHON)______________
'''
What kind of value a variable can store
how much memory it needs
what operations can be performed on it
'''
x=10
y=3.14
z="Hello"

# ================================
# ================================



'''
Python is dynamically typed:
___You don't declare data type explicity.
___python decides the type at run time.

'''
# ================================
# ================================



'''
___________(BUILT-IN DATA TYPES IN PYTHON)____________
Python has:
01__Numeric(int-float-complex)
02__Boolean(bool)
03__Text(str)
04__Sequence(list-tuple-range)
05__Set(set-frozenset)
06__Mapping(dict)
07__Binary(bytes,bytearray,memoryview)
08__None(None Type)
'''

# ================================
# ================================



#___________(NUMERIC DATA TYPES)____________
#int(whole number, it can be positive or negative)
salary=80000
print(salary)
age=24
print(age)
any_number=-123456789123456789
print(any_number)
#float(Decimal/real numbers,it can be negative or positive)
PI=3.14
print(PI)
num=-0.001
print(num)
tax=5.3
print(tax)
z=1.2e3
print(z)
#complex(Numbers with real and imaginary parts)
vector=3+5j
print(vector.real)
print(vector.imag)
'''
#complex data types are used in:
___Signal processing
___Engineering
___Scientific computing
'''

# ================================
# ================================



#___________(BOOLEAN DATA TYPES)____________
#bool(only two values, True==1 and False==0)
is_married=False  #output 0
print(is_married)
is_singal=True    #output 1
print(is_singal)

# ================================
# ================================



#___________(TEXT DATA TYPES)____________
#str(Sequence of unicode characters[0-255])
name="muhammad hassan raza"
print(name)
dept="Software engineering"
print(dept)

# ================================
# ================================


#___________(SEQUENCE DATA TYPES)____________
#list(collection of items, written in square brackets[], lists are ordered,mutable and allow duplicates)
core_subjects=["fundament programming","oop","DSA","databases","operating system"]
print(core_subjects)
#used for dynamic collections and real world data storage

#tuple(collection of items, written in praenthesis(), tuples are ordered, immutable and allow duplicates and also faster than lists)
point=(10,20)
print(point)
#used for fixed data and dictionary keys

#range(immutable sequence of numbers)
#range(start value(include),end value(exclude),increment/decrement)
#used with for loop
for i in range(10): #default start from 0 and end on 9
    print(i)

for i in range(3,11):  #start from 3 and end on 10
    print(i) 

for i in range(2,16,3): # start from 2 and increment of 3 until 16 is reached
    print(i)

# ================================
# ================================


#___________(SET DATA TYPES)__________
#SET: unordered, no duplicate, mutable, written inside {}, 
#different operations on it are: union, intersection and difference
set={1,2,3,4,5,6}
#FROZENSET: immutable version of set
fs=frozenset([1,2,3])
#used when set needs to be a dictionary key.

# ================================
# ================================



#___________(MAPPING DATA TYPES)__________
#DICTIONARY(dict): key:value pairs , keys must be immutable.
student={
    "name":"Hassan raza",
    "age": 21,
    "cgpa":3.48
}
#access:
student["name"]
student["age"]
student["cgpa"]

student.get("name")
student.get("age")
student.get("cgpa")
#used in: JSON,APIS,DATABASES, REAL WORLD SYSTEMS

# ================================
# ================================



#___________(BINARY DATA TYPES)__________
#BYTES: immutable binary data
b=b"hello"
#bytearray: Mutable binary data.
ba=bytearray(b"hello")
ba[0]=72
#memoryview: veiw of binary data without copying 
mv=memoryview(b"hello")
#used in: networking, file handling and performance-critical systems

# ================================
# ================================



#___________(NONE DATA TYPES)__________
#None: represents absence of value.
x=None
#used for: initialization,default return values and optional data.