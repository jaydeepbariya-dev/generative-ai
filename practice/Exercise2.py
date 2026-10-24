
# ============================================================
# DAY 2 - STEP 3: PRACTICE
# Total: 10 Marks
# ============================================================


# Q1. CONDITIONAL STATEMENTS (1.5 marks)
# Classify each employee based on salary.

salaries = [35000, 55000, 90000, 45000, 75000]

for salary in salaries:
    if salary >= 80000:
        print(f"{salary} -> High Salary")
    elif salary >= 50000:
        print(f"{salary} -> Medium Salary")
    else:
        print(f"{salary} -> Low Salary")


# Q2. LOOPS (1.5 marks)
# 1. Calculate sum of all numbers.
# 2. Count numbers divisible by 3.
# 3. Skip negative numbers using continue.

numbers = [10, -5, 9, 12, -2, 15, 20]

total = 0
count = 0

for number in numbers:

    if number < 0:
        continue

    total += number

    if number % 3 == 0:
        count += 1

print("Sum:", total)
print("Count divisible by 3:", count)


# Q3. LIST COMPREHENSION (2 marks)
# 1. Increase every price by 18% GST.
# 2. Filter prices above 1000.

prices = [500, 1200, 800, 2000, 1500]

# Add 18% GST to every price
new_prices = [price + (price * 0.18) for price in prices]

# Filter prices greater than 1000
new_prices_one = [price for price in new_prices if price > 1000]

print("Prices after GST:", new_prices)
print("Prices above 1000:", new_prices_one)


# Q4. TUPLES (1 mark)
# 1. Print first and last elements.
# 2. Print number of elements.
# 3. Convert tuple into a list and add a skill.

skills = ("Java", "Python", "SQL", "AWS")

print("First skill:", skills[0])
print("Last skill:", skills[-1])
print("Number of skills:", len(skills))

skills_list = list(skills)
skills_list.append("Spring")

print("Updated skills:", skills_list)


# Q5. DICTIONARIES (2 marks)
# 1. Print employee names and salaries.
# 2. Find employee with highest salary.
# 3. Calculate average salary.

employees = {
    "emp1": {"name": "Amit", "salary": 60000},
    "emp2": {"name": "Rahul", "salary": 80000},
    "emp3": {"name": "Neha", "salary": 70000}
}

max_salary = 0
highest_paid_employee = ""
total_salary = 0

for key, value in employees.items():

    # Extract name and salary from inner dictionary
    name = value["name"]
    salary = value["salary"]

    print(f"{name} -> {salary}")

    # Calculate total salary
    total_salary += salary

    # Find highest paid employee
    if salary > max_salary:
        max_salary = salary
        highest_paid_employee = name

average_salary = total_salary / len(employees)

print("Highest Paid Employee:", highest_paid_employee)
print("Highest Salary:", max_salary)
print("Average Salary:", average_salary)


# Q6. SETS (2 marks)
# 1. Find all unique skills.
# 2. Find common skills.
# 3. Find skills present only in first list.

skills1 = ["Java", "Python", "SQL", "Java"]
skills2 = ["Python", "AWS", "SQL", "Docker"]

# Convert lists into sets
set1 = set(skills1)
set2 = set(skills2)

# Perform set operations
unique_skills = set1.union(set2)
common_skills = set1.intersection(set2)
first_only_skills = set1.difference(set2)

print("Unique Skills:", unique_skills)
print("Common Skills:", common_skills)
print("First List Only:", first_only_skills)


# ============================================================
# END OF PRACTICE
# ============================================================
