#Write a program that prompts the user to enter the base and height of a triangle and returns its area.
#base = float(input("Enter the base of the triangle: "))
#height = float(input("Enter the height of the triangle: "))

#area = base * height
        
#print (area)

#number 2
#number = int(input("Please enter a number: ")) # prompt user for input and convert to integer

#if number % 2 == 0:
 #   print("Even")
#else:
#    print("Odd")
  
  #number 3


#Get phone number from user
#phonenumber = input("Enter your phone number: ")

# Validate the phone number
#if phonenumber.startswith(('+254', '254', '07', '71', '01')) and phonenumber.isdigit():
   #  Convert to international format if needed
 #   if phonenumber.startswith(('254', '01')):
  #      phone_number = '+254' + phonenumber[3:]
   # elif phonenumber.startswith('07'):
    #    phonenumber = '+254' + phonenumber[1:]
    #elif phonenumber.startswith('71'):
     #   phonenumber = '+254' + phonenumber[1:]
    #print("Valid phone number: ", phonenumber)
#else:
 #   print("Invalid phone number!")

#number 4

#if "@" in email and "." in email:
    #print("Email is valid.")
#else:
    #print("Email is invalid.") 

#task 5 

# take user inputs from the terminal #notes
#num1 = int(input("Enter the first number: "))
#num2 = int(input("Enter the second number: "))
#num3 = int(input("Enter the third number: "))

# initialize a variable to store the largest number(#notes)
#largest = num1

# check if num2 is larger than the current largest(#notes)
#if num2 > largest:
#    largest = num2

# check if num3 is larger than the current largest
#if num3 > largest:
#    largest = num3

# print the largest number
#print("The largest number is:", largest)

   

#task 6
#password = "admin@123"
#attempts = 4

#while attempts > 0:
 #   user_input = input("Enter password: ")
  #  if user_input == password:
   #     print("Access granted")
    #    break
    #else:
     #   attempts -= 1
#      #  print(f"Wrong password. {attempts} attempt(s) left.")
#else:
 #
 #    print("Account blocked.")


#task 7

#marks = int(input("Enter the student's marks (between 0 and 100): "))

#if marks > 79:
 #   grade = 'A'
#elif marks >= 60 and marks <= 79:
 #   grade = 'B'
#elif marks >= 50 and marks <= 59:
 #   grade = 'C'
#elif marks >= 40 and marks <= 49:
 #   grade = 'D'
#else:
 #   grade = 'E'

#print("The student's grade is:", grade)


#task 8

#speed = int(input("Enter the speed of the car: "))

#if speed < 70:
 #   print("Ok")
#else:
 #   demerit_points = (speed - 70) // 5
  #  if demerit_points > 12:
   #     print("License suspended")
    #else:
     #   print("Points:", demerit_points)

#task 9

#rows = int(input("Enter the number of rows: "))

#for i in range(1, rows+1):
 #   print("*" * i)


#task 10
#prods = [['omo','30kshs','300'], ['milk','50kshs','200'],['bread','45kshs','359'], ['coffee','5kshs','79']]

#total_stock = 0

#for item in prods:
 #   stock = int(item[-1]) # convert the last element of each item to an integer
  #  total_stock += stock

#print("Total stock in the company is:", total_stock)

#task 11
#from datetime import datetime, date

#def calculate_age(birthdate):
 #   today = date.today()
  #  age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
   #3 return age

#def age_in_years_months_days(birthdate):
 #   today = date.today()
  #  age_years = today.year - birthdate.year
   # age_months = today.month - birthdate.month
    #age_days = today.day - birthdate.day

    # adjust for negative age_months and age_days(#notes)
    #if age_days < 0:
     #   last_month = today.replace(day=1) - datetime.timedelta(days=1)
      #  age_days += (today - last_month).days
       # age_months -= 1
    #if age_months < 0:
     #   age_months += 12
      #  age_years -= 1

    #return age_years, age_months, age_days

#birthdate = datetime.strptime(input("Enter your birthdate (in format yyyy-mm-dd): "), "%Y-%m-%d").date()
#age = calculate_age(birthdate)
#age_years, age_months, age_days = age_in_years_months_days(birthdate)

#print("Your age is:", age, "years old")
#print("That's", age_years, "years,", age_months, "months, and", age_days, "days")


#task 12

#num1 = float(input("Enter the first number: "))
#num2 = float(input("Enter the second number: "))
#num3 = float(input("Enter the third number: "))
#num4 = float(input("Enter the fourth number: "))

#if num1 > num2 and num1 > num3 and num1 > num4:
 #   print("The largest number is:", num1)
#elif num2 > num1 and num2 > num3 and num2 > num4:
 #   print("The largest number is:", num2)
#elif num3 > num1 and num3 > num2 and num3 > num4:
 #   print("The largest number is:", num3)
#else:
 #   print("The largest number is:", num4)

#task 13

#email = input("Enter your email: ")
#password = input("Enter your password: ")
#attempts = 1

#while email != "admin@mail.com" or password != "Admin@123":
 #   if attempts >= 3:
  #      print("You have been blocked. Please contact support.")
   #     break
    #print("Invalid username or password. Please try again.")
    #email = input("Enter your email: ")
    #password = input("Enter your password: ")
    #attempts += 1
#else:
 #   print("Login is Successful")


#task 14
#while True:
 #   try:
  #      num1 = float(input("Enter the first number: "))
   #     num2 = float(input("Enter the second number: "))
    #    result = num1 + num2
     #   print("The sum is", result)
      #  break
    #except ValueError:
     #   print("Invalid character entered. Please enter numbers or floats only.")

#task 15

# Get user input for basic salary and benefits(#notes)

#basic_salary = float(input("Enter basic salary: "))
#benefits = float(input("Enter benefits: "))

#(notes) Calculate gross salary

#gross_salary = basic_salary + benefits

#(notes) Determine NHIF based on gross salary

#if gross_salary <= 6000:
 #   nhif = 150
#elif gross_salary <= 8000:
 #   nhif = 300
#elif gross_salary <= 12000:
 #   nhif = 400
#elif gross_salary <= 15000:
 #   nhif = 500
#elif gross_salary <= 20000:
 #   nhif = 600
#elif gross_salary <= 25000:
 #   nhif = 750
#elif gross_salary <= 30000:
 #   nhif = 850
#elif gross_salary <= 35000:
 #   nhif = 900
#elif gross_salary <= 40000:
 #   nhif = 950
#else:
#    nhif = 1000

#print(f"Gross Salary: {gross_salary}")
#print(f"NHIF: {nhif}")

#task 16

def gross_salary(i, b):
    gross_income=i + b
    return gross_income

def nssf(ti):
    nssf=ti * 0.06
    return nssf

def nhif(gross_income):
    nhif= 0
    if gross_income <= 5999:
       nhif=150
    elif gross_income >=6000 and gross_income < 7999:
       nhif = 300
    elif gross_income >= 8000 and gross_income < 11999:
        nhif = 400
    elif gross_income >= 12000 and gross_income < 14999:
       nhif = 500
    elif gross_income >= 15000 and gross_income < 19999:
       nhif = 600
    elif gross_income >= 20000 and gross_income < 24999:
        nhif = 750
    elif gross_income >= 25000 and gross_income < 29999:
         nhif = 850
    else:
        nhif is 1050
    return nhif

def payee():
     


income=float(input("Enter the basic salary :"))
benefits=float(input("Benefits :"))

g=gross_salary(income, benefits)
nssf=nssf(g)
nhif=nhif(g)


print(g)
print(nssf)
print(nhif)













  








    
     
