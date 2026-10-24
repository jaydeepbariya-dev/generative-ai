
# ============================================================
# DAY 2 - STEP 4: EMPLOYEE MANAGEMENT SYSTEM
# ============================================================

employees = {
    "1": {"name": "Jaydeep", "age": 26, "department": "IT", "salary": 100},
    "2": {"name": "Manoj", "age": 27, "department": "Commerce", "salary": 50},
    "3": {"name": "Sandhya", "age": 22, "department": "Govt", "salary": 80},
    "4": {"name": "Dharam", "age": 23, "department": "Business", "salary": 70}
}


# 1. Display all employee details

print("\n--- ALL EMPLOYEES ---")

for key, value in employees.items():
    print(f"\nEmployee ID: {key}")
    print(f"Name: {value['name']}")
    print(f"Age: {value['age']}")
    print(f"Department: {value['department']}")
    print(f"Salary: {value['salary']}")


# 2. Find employee with the highest salary

highest_salary = 0
highest_paid_employee = ""

for key, value in employees.items():
    if value["salary"] > highest_salary:
        highest_salary = value["salary"]
        highest_paid_employee = value["name"]

print("\n--- HIGHEST PAID EMPLOYEE ---")
print("Name:", highest_paid_employee)
print("Salary:", highest_salary)


# 3. Calculate average salary

total_salary = 0

for key, value in employees.items():
    total_salary += value["salary"]

avg_salary = total_salary / len(employees)

print("\n--- AVERAGE SALARY ---")
print(avg_salary)


# 4. Display employees earning more than 50

print("\n--- EMPLOYEES EARNING MORE THAN 50 ---")

for key, value in employees.items():
    if value["salary"] > 50:
        print(value["name"], value["salary"])


# 5. Store unique department names using a set

departments = set()

for key, value in employees.items():
    departments.add(value["department"])

print("\n--- UNIQUE DEPARTMENTS ---")
print(departments)


# 6. Search employee by name

search_name = input("\nEnter employee name to search: ")

found = False

for key, value in employees.items():
    if value["name"].lower() == search_name.lower():
        print("\nEmployee Found!")
        print("Employee ID:", key)
        print("Details:", value)
        found = True
        break

if not found:
    print("Employee not found")


# ============================================================
# END OF PROJECT
# ============================================================
