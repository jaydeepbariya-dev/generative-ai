
# ============================================================
# DAY 2 - STEP 2: IMPLEMENTATION
# Topics: Conditionals, Loops, Lists, Tuples, Dictionaries, Sets
# Total: 10 Marks
# ============================================================


# Q1. CONDITIONAL STATEMENTS (1.5 marks)
# Given an employee's salary:
# - Salary >= 80000: Print "Senior Level"
# - Salary >= 50000: Print "Mid Level"
# - Otherwise: Print "Junior Level"

salary = 65000

# Write your code here
if salary >= 80000:
    print("Senior Level")
elif salary >= 50000:
    print("Mid Level")
else:
    print("Junior Level")


# Q2. LOOPS AND LOOP CONTROL (1.5 marks)
# Given a list of numbers:
# - Print only even numbers.
# - Skip number 5 using continue.
# - Stop the loop when you encounter 10 using break.

numbers = [2, 5, 7, 8, 10, 12, 14]

# Write your code here
for number in numbers:

    if number == 10:
            break 

    if number == 5:
            continue

    if number % 2 == 0:
        print(number)
    
        


# Q3. LISTS AND LIST COMPREHENSION (2 marks)
# Given a list of employee salaries:
# 1. Add 5000 to every salary using list comprehension.
# 2. Create a new list containing salaries greater than 50000.
# 3. Print the total number of employees.

salaries = [30000, 45000, 60000, 75000, 40000]

# Write your code here
salaries.append(5000)

new_salaries = [salary for salary in salaries if salary >= 50000]
print(salaries.len())


# Q4. TUPLES (1 mark)
# Create a tuple containing:
# employee name, employee age, employee department.
# 1. Print the employee name.
# 2. Print the employee department.
# 3. Try to explain whether you can modify a tuple after creation.

# Write your code here
tup = ("Jaydeep", 26, "IT")
print(tup[0])
print(tup[2])

# No we cannot. As they are immutable by nature

# Q5. DICTIONARIES (2 marks)
# Create an employee dictionary with:
# name, age, department, salary.
#
# 1. Print the employee name using get().
# 2. Update the salary to 75000.
# 3. Add a new key "location" with value "Ahmedabad".
# 4. Print all key-value pairs using items().

# Write your code here
dict = {
     "name": "Jaydeep",
     "age": 26,
     "dept": "IT",
     "salary": 100 
}

print(dict.get("name"))
dict["salary"] = 75000
dict["location"] = "Ahmedabad"

for key, value in dict.items():
     print(f"{key} -> {value}")

# Q6. SETS (2 marks)
# Given two sets of employee skills:
# 1. Find all unique skills across both sets.
# 2. Find common skills.
# 3. Find skills present in the first set but not the second.

employee1_skills = {"Java", "Python", "SQL", "Spring"}
employee2_skills = {"Python", "AWS", "SQL", "Docker"}

# Write your code here
unique_skills = employee1_skills.union(employee2_skills)
common_skills = employee1_skills.intersection(employee2_skills)
diff_skills = employee1_skills.difference(employee2_skills)

# ============================================================
# END OF EXERCISES
# ============================================================
