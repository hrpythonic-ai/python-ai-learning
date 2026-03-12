#__________________(VARIABLES IN PYTHON)__________________
#What is a variable: A variable is a name that stores a value.
num=10
#num is variable and it stores a value 10.



#A variable is:

'''
01_A name (identifier)
02_That points/references to a value
03_Inside the computer's memory (RAM)
'''

# ================================
# ================================



#C++ (Variable = Box that stores value directly)
#The variable contains the value inside its own memory box.
#Changing the variable changes the value inside the same box.
'''
+------------+
|  x : 10    |
+------------+
'''

# ================================
# ================================




#_____________(Two variables contain same value)______________
#C++ (Two Variables = Two Boxes, Each Stores Its Own Value)
#Each variable has its own separate memory box.
#Copying a variable creates a new box with the same value.
'''
+------------+      +------------+
|  a : 10    |      |  b : 10    |
+------------+      +------------+

'''

# ================================
# ================================



#_____________(Two variables contain same value)______________
#Python (Two Variables = Two Labels Pointing to One Box)
#Assigning b = a makes both variables point to the same object.
#No new value box is created unless reassigned.
'''
a ───►
       +--------+
b ───► |  10    |
       +--------+

'''

# ================================
# ================================



#___________(Python Variables Are Dynamically Typed)______________
#Python is a dynamically typed language.
#You do not need to declare the data type.
#Python decides the type automatically at runtime.
x = 10       # x becomes an integer
x = "Hello"  # x becomes a string


# ================================
# ================================




#________________(How Variables Are Stored in Memory)__________________

#Every value in Python is an object.
#Every object has:
'''
01__ID (memory address)

02__Type

03__Value
'''
x = 10
print(id(x))     # memory address of value 10
print(type(x))   # <class 'int'>
print(x)         # 10


# ================================
# ================================



#_____________(Variables Are Case-Sensitive)_____________
age = 10
Age = 20
AGE = 30
#All are different variables.


# ================================
# ================================




#_________________(Assigning values)________________
#declare variable:
#python does not allow declaring without assigning values like x
#assigning value:
#x=10 when you assign a value of 10 to variable x, then it works in python.
x=10
print(x)


# ================================
# ================================



#______________(print value of variable)____________
#when you want to print variable, you do'nt need of single ' ' or double quotation " ".
#you print variable without quotations.


# ================================
# ================================



#single line assignment:
x=10
print(x)
#different/multiple variables, same value(one value)
x=y=z=10
print(x)
print(y)
print(z)
#different/multiple variables, different values
x,y,z=3,5,7
print(x)
print(y)
print(z)


# ================================
# ================================



#________(which type of values a variable can store in python)________________
'''
01__int
02__float
03__string
04__boolean
05__list
06__tuple
07__dictionary
08__set
09__None
10__functions
11__objects
'''

# ================================
# ================================




'''
| Category           | Data Type            | Example                   | Description             |
| ------------------ | -------------------- | ------------------------- | ----------------------- |
| **Numeric**        | `int`                | `x = 10`                  | Whole numbers           |
|                    | **Binary int**       | `x = 0b1010`              | Base-2 integer          |
|                    | **Octal int**        | `x = 0o17`                | Base-8 integer          |
|                    | **Hex int**          | `x = 0x1A`                | Base-16 integer         |
|                    | `float`              | `x = 3.14`                | Decimal numbers         |
|                    | `complex`            | `x = 4+5j`                | Complex numbers         |
| **Text**           | `str`                | `"Ali"`                   | Unicode characters      |
| **Boolean**        | `bool`               | `True` / `False`          | Logical values          |
| **Sequence**       | `list`               | `[1,2,3]`                 | Mutable sequence        |
|                    | `tuple`              | `(1,2,3)`                 | Immutable sequence      |
|                    | `range`              | `range(5)`                | Sequence of numbers     |
| **Mapping**        | `dict`               | `{"a":1}`                 | Key-value pairs         |
| **Set Types**      | `set`                | `{1,2,3}`                 | Unordered unique values |
|                    | `frozenset`          | `frozenset([1,2,3])`      | Immutable set           |
| **Binary Types**   | `bytes`              | `b"ABC"`                  | Immutable bytes         |
|                    | `bytearray`          | `bytearray([65,66])`      | Mutable bytes           |
|                    | `memoryview`         | `memoryview(b"ABC")`      | View of byte buffer     |
| **Special Types**  | `NoneType`           | `None`                    | No value                |
|                    | `EllipsisType`       | `...`                     | Used in slicing/typing  |
|                    | `NotImplementedType` | `NotImplemented`          | Used in operators       |
| **Callable Types** | Function             | `def f(): pass`           | A function object       |
|                    | Lambda               | `lambda x: x+1`           | Anonymous function      |
| **OOP Types**      | Class                | `class A: pass`           | User defined type       |
|                    | Object               | `obj = A()`               | Instance of class       |
| **Advanced Types** | Generator            | `(x*x for x in range(5))` | Lazy sequence           |
|                    | Iterator             | `iter([1,2,3])`           | Iterates elements       |
|                    | Module               | `import math`             | Module object           |
|                    | File Object          | `open("a.txt")`           | File handler            |
| **External Types** | NumPy Array          | `np.array([1,2])`         | Numeric array           |
|                    | Pandas DataFrame     | `pd.DataFrame()`          | Tabular data            |

'''

# ================================
# ================================



'''
| Category           | Data Type            | Example                   | Description             |
| ------------------ | -------------------- | ------------------------- | ----------------------- |
| **Numeric**        | `int`                | `x = 10`                  | Whole numbers           |
|                    | **Binary int**       | `x = 0b1010`              | Base-2 integer          |
|                    | **Octal int**        | `x = 0o17`                | Base-8 integer          |
|                    | **Hex int**          | `x = 0x1A`                | Base-16 integer         |
|                    | `float`              | `x = 3.14`                | Decimal numbers         |
|                    | `complex`            | `x = 4+5j`                | Complex numbers         |
| **Text**           | `str`                | `"Ali"`                   | Unicode characters      |
| **Boolean**        | `bool`               | `True` / `False`          | Logical values          |
| **Sequence**       | `list`               | `[1,2,3]`                 | Mutable sequence        |
|                    | `tuple`              | `(1,2,3)`                 | Immutable sequence      |
|                    | `range`              | `range(5)`                | Sequence of numbers     |
| **Mapping**        | `dict`               | `{"a":1}`                 | Key-value pairs         |
| **Set Types**      | `set`                | `{1,2,3}`                 | Unordered unique values |
|                    | `frozenset`          | `frozenset([1,2,3])`      | Immutable set           |
| **Binary Types**   | `bytes`              | `b"ABC"`                  | Immutable bytes         |
|                    | `bytearray`          | `bytearray([65,66])`      | Mutable bytes           |
|                    | `memoryview`         | `memoryview(b"ABC")`      | View of byte buffer     |
| **Special Types**  | `NoneType`           | `None`                    | No value                |
|                    | `EllipsisType`       | `...`                     | Used in slicing/typing  |
|                    | `NotImplementedType` | `NotImplemented`          | Used in operators       |
| **Callable Types** | Function             | `def f(): pass`           | A function object       |
|                    | Lambda               | `lambda x: x+1`           | Anonymous function      |
| **OOP Types**      | Class                | `class A: pass`           | User defined type       |
|                    | Object               | `obj = A()`               | Instance of class       |
| **Advanced Types** | Generator            | `(x*x for x in range(5))` | Lazy sequence           |
|                    | Iterator             | `iter([1,2,3])`           | Iterates elements       |
|                    | Module               | `import math`             | Module object           |
|                    | File Object          | `open("a.txt")`           | File handler            |
| **External Types** | NumPy Array          | `np.array([1,2])`         | Numeric array           |
|                    | Pandas DataFrame     | `pd.DataFrame()`          | Tabular data            |

'''

# ================================
# ================================



'''
PYTHON DATA TYPES
│
├── NUMERIC
│   ├── int
│   │   ├── binary (0b)
│   │   ├── octal (0o)
│   │   └── hex (0x)
│   ├── float
│   └── complex
│
├── TEXT
│   └── str
│
├── BOOLEAN
│   └── bool
│
├── SEQUENCE TYPES
│   ├── list
│   ├── tuple
│   └── range
│
├── MAPPING
│   └── dict
│
├── SET TYPES
│   ├── set
│   └── frozenset
│
├── BINARY TYPES
│   ├── bytes
│   ├── bytearray
│   └── memoryview
│
├── SPECIAL TYPES
│   ├── NoneType
│   ├── EllipsisType (...)
│   └── NotImplementedType
│
├── CALLABLE TYPES
│   ├── function
│   ├── lambda
│   └── built-in functions
│
├── OOP TYPES
│   ├── class
│   └── object (instance)
│
├── ADVANCED TYPES
│   ├── generator
│   ├── iterator
│   ├── module
│   └── file
│
└── EXTERNAL LIBRARY TYPES
    ├── NumPy array
    ├── Pandas DataFrame
    ├── TensorFlow tensors
    └── PyTorch tensors

'''


# ================================
# ================================



#________________(scope of variables)________________
#01_local variable->A local variable is created inside a function and can only be used inside that function.
def my_function():
    x = 10   # Local variable
    print("Inside function, x =", x)

my_function()

# This will give an error:
# print(x)   # x is not accessible outside the function

#02_global variable->A global variable is created outside any function and can be used both outside and inside of the function.
y = 20   # Global variable
def show_global():
    print("Inside function, y =", y)

show_global()
print("Outside function, y =", y)

#03_Create a Global Variable Inside a Function->You can create or modify a global variable from inside a function using the global keyword.
def create_global():
    global z      # Declaring z as global inside function
    z = 30        # Now z becomes a global variable
    print("Inside function, z =", z)

create_global()
print("Outside function, z =", z)

#global z tells Python that z should be treated as a global variable.
#Even though z is created inside the function:
#It becomes available everywhere in the program.


# ================================
# ================================



#___________(rules of variable names)_____________
'''
01_variable names contain only underscore(_), numbers(0-9) and alphabets([a-z][A-Z]).
02_variable names cannot start with digits.
03_variable names are only start with underscore(_) and alphabets([a-z][A-Z]).
04_variable names does not contain spaces, or any special character except underscore.
05_variable names are case sensitive age, Age and AGE are different variables.
06_variable names does not use keyword or reserved words in python.
'''

# ================================
# ================================



'''
| Case Type      | Style                            | Example     | Allowed in Python?       |
| -------------- | -------------------------------- | ----------- | ------------------------ |
| **snake_case** | lowercase_words_with_underscores | `user_name` | ✔ Yes                    |
| **camelCase**  | firstWordLowerNextWordsUpper     | `userName`  | ✔ Yes                    |
| **PascalCase** | EachWordStartsUppercase          | `UserName`  | ✔ Yes (classes)          |
| **kebab-case** | lowercase-words-with-hyphens     | `user-name` | ❌ No (invalid in Python)|
'''



















