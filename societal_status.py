import json
import datetime as dt
from datetime import timedelta


today_date = dt.datetime.now()
one_month_duration = timedelta(weeks = 4)
next_month_date = today_date + one_month_duration

# User Variables
uber_credits = 0

# Status checker for user

working_student = 0
poverty = 0
accommodation = 0

# Check for working/student status

def check_status_working_student():
    global working_student

    if working_student == 0:
        verification = 0
        student_id = input("\nPlease enter your student ID number: ")
        print("\nYour student ID is:", student_id)

        # Needs error handling for student verification
        print("\nWe are currenly checking your student status, please give one business day for a response.")
        verification += 1

        if verification == 1:
            working_student += 1
            return working_student
        else:
            print("\nUnfortunately, we weren't able to process your applications\n"
                       "Please contact customer support: (012-223-223)")



def check_status_poverty():
    global poverty
    global uber_credits

    if poverty == 0:
        annual_income = int(input("\nPlease enter your estimate annual income: $ "))
        print("\nYour annual income is: $",annual_income)
        print("\nThe system is processing numbers.....")
        if annual_income <= 24000:
            print("\nYou are eligible to $70.00 of Uber Credits per month starting from", dt.datetime.now(),"\n"
                  "until", next_month_date, "\n")
            uber_credits += 70.00
            poverty += 1
            
        else:
            print("\nUnfortunately, we weren't able to process your applications\n"
                       "Please contact customer support: (012-223-223)")
            
def check_status_accommodation():
    global accommodation

    if accommodation == 0:

        # Needs fixed input of 1 character

        help = input("Do you require accommodation when riding with Uber (Y/N): ")

        if help == "Y":
            accommodation += 1
            print("\nWe will notify our drivers about your accommodation.")
        else:
            accomodation = 0
            return accommodation

# Calling the functions

check_status_working_student()
check_status_poverty()
check_status_accommodation()
print("\nWorking Student: ", working_student, "\nFinancial Aid: ", poverty , "\nRequires Accommodation", accommodation)

#--------------------------------

# THIS NEEDS IMPROVEMENT AND FUNCTIONALITY

# Json Dump Files
users = {}
users['info'] = []

# Create a dictionary with user information
user_info = {
    "working_student": working_student,
    "poverty": poverty,
    "accommodation": accommodation,
}

file_name = "user_info.json"

with open(file_name, "w") as json_file:
    json.dump(user_info, json_file, indent=4)

print(f"User information has been saved to {file_name}")
print(user_info)

