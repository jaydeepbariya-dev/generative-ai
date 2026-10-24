
# ============================================================
# DAY 1 - PYTHON FUNDAMENTALS
# STEP 2 - HANDS-ON IMPLEMENTATION
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1: VARIABLES AND DATA TYPES
# ------------------------------------------------------------
# Create variables for an employee:
# 1. Employee name
# 2. Employee age
# 3. Employee salary
# 4. Is the employee currently working?
#
# Print each variable along with its data type.


# Write your solution below:
employee_name = "Jaydeep"
employee_age = 26
employee_salary = 11.3
employee_working = True 
print(f"{employee_name} {type(employee_name)}")
print(f"{employee_age} {type(employee_age)}")
print(f"{employee_salary} {type(employee_salary)}")
print(f"{employee_working} {type(employee_working)}")

# ------------------------------------------------------------
# EXERCISE 2: TYPE CONVERSION
# ------------------------------------------------------------
# Given:
age = "28"
salary = "75000.50"
#
# Requirements:
# 1. Convert age into an integer.
# 2. Convert salary into a float.
# 3. Print their sum.


# Write your solution below:
age_int = int(age)
salary_float = float(salary)
print(age_int)
print(salary_float)

# ------------------------------------------------------------
# EXERCISE 3: ARITHMETIC OPERATORS
# ------------------------------------------------------------
# Given:
# a = 25
# b = 4
#
# Calculate and print:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Floor division
# 6. Modulus
# 7. Exponentiation


# Write your solution below:
a = 25
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# ------------------------------------------------------------
# EXERCISE 4: COMPARISON AND LOGICAL OPERATORS
# ------------------------------------------------------------
# Given:
# age = 27
# experience = 4
# is_java_developer = True
#
# Evaluate and print:
# 1. Is age greater than 25?
# 2. Is experience at least 3 years?
# 3. Is the employee a Java developer AND has at least
#    3 years of experience?
# 4. Is the employee older than 30 OR has more than
#    5 years of experience?


# Write your solution below:
age = 27
experience = 4
is_java_developer = True
print(age > 25)
print(experience >= 3)
print(is_java_developer == True and experience >= 3)
print(age > 30 or experience > 5)

# ------------------------------------------------------------
# EXERCISE 5: EMPLOYEE SALARY CALCULATOR
# ------------------------------------------------------------
# Given:
# basic_salary = 50000
#
# Requirements:
# 1. Calculate HRA = 20% of basic salary.
# 2. Calculate bonus = 10% of basic salary.
# 3. Calculate total salary.
# 4. Print basic salary, HRA, bonus and total salary.


# Write your solution below:
basic_salary = 50000
hra = 0.20 * basic_salary
bonus = 0.10 * basic_salary
total_salary = basic_salary + hra + bonus
print(basic_salary)
print(hra)
print(bonus)
print(total_salary)


# ------------------------------------------------------------
# EXERCISE 6: SKILL MEMBERSHIP CHECKER
# ------------------------------------------------------------
# Given:
# skills = ["Java", "Spring Boot", "Python", "SQL", "Docker"]
#
# Requirements:
# 1. Check whether Python is present.
# 2. Check whether JavaScript is absent.
# 3. Check whether SQL is present.
#
# Use membership operators (in and not in).


# Write your solution below:
skills = ["Java", "Spring Boot", "Python", "SQL", "Docker"]
print("Python" in skills)
print("JavaScript" not in skills)
print("SQL" in skills)

# ============================================================
# END OF DAY 1 - STEP 2
# ============================================================
