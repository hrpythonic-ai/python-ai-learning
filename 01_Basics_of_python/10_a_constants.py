# ================================
#CONSTANTS IN PYTHON
# ================================
#Constant: A constant is a variable whose value should not change, once assigned.
#aise variables jin ki value fixed ho
'''
01_value of pi
02_Speed of light
03_Number of days in a week(7)
04_Number of months in a year(12)
'''

# ================================
# ================================



#________________(HOW CONSTANTS ARE CREATED IN PYTHON?)
#Python use UPPERCASE variable names to indicate constants.
PI=3.14159
GRAVITY=9.8
MAX_USERS=100

# ================================
# ================================



#Bad practice:
r=3
area=3.14*r*r
print(area)
#Good practice:
r=3
PI=3.14159
area=PI*r*r
print(area)

# ================================
# ================================



#____________(TYPES OF CONSTANTS IN PYTHON)___________________
#NUMERIC CONSTANTS
MAX_SPEED=120
PI=3.14159
TEMPRATURE=-273.15
#STRING CONSTANTS
APP_NAME="Student Management System"
DEFAULT_PASSWORD="admin123"
#BOOLEAN CONSTANTS
DEBUG=True
IS_PRODUCTION=False
#COLLECTION CONSTANTS
#make sure that when you make collection:
#_01___
#does not make in list because list is mutalbe but you know you cannot change the value of constant(fixed value):
COLORS=["red","green","blue"]
#its fine but when you want to change this value it is wrong or it is not possible becuse list can be channged  but constant cannot be changed.
'''
COLORS.append("Yellow") #error
'''
#_02___
#collection make as tuple becauce it is immutable and constants are also fixed.
COLORS=("red","green","blue")

# ================================
# ================================




#____________(CONSTANTS USING MODULES-->BEST PRACTICES IN INDUSTORY)_________
'''
Create a constant file : constants.py
import constants from constant file --> To main.py
like that:
____________
constants.py
_______
PI=3.14159
GRAVITY=9.8
MAX_USERS=100
_____________
main.py
________
import constants
r=3
area_of_circle=constants.PI*r**2
print(area_of_circle)
'''
# ================================
# ================================



#_____________(PREVENTING CHANGES --> ADVANCED TECHNIQUES)
#METHOD:01:__________Using tuples___________
DAYS=("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
#METHOD:02:__________Using typing.Final_________
from typing import Final
PI:Final=3.14159
#METHOD:03:__________Custom Constant Class_________
class Constants:
    PI=3.14159
    def _setter_(self,name,value):
        raise
AttributeError("cannot modify constant")
const=Constants()

# ================================
# ================================




#____________(CONSTANTS IN REAL WORLD PROJECTS)____________
#WEB DEVELOPMENTS
BASE_URL="https://api.example.com"
TIMEOUT=30
#MACHINE LEARNING
LEARNING_RATE=0.01
EPOCHS=100
#BANKING SYSTEM
MIN_BALANCE=500
INTEREST_RATE=0.05

# ================================
# ================================



#__________(DIFFERENCE BETWEEN VARIABLES AND CONSTANTS)
#variable: can change,lower case,dynamic data
#CONSTANTS: cannot change, UPPERCASE, fixed value
