def say_hi():
    print("hello user")
say_hi()
#-------------------------------
#-------------------------------
def ask_age_and_check_eligibility():
    age=int(input("Enter your age: "))
    if age>=18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
ask_age_and_check_eligibility()
#-------------------------------
#-------------------------------
def check_age_eligibility(age,domicile):
    domicile=domicile.lower()
    if age>=18 and domicile=='lahore':
        print("You're eligible to vote.")
    else:
        print("You're not eligible to vote.")
check_age_eligibility()
#-------------------------------
#-------------------------------
