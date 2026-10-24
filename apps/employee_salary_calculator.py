"""
Build a program that:
1. Accepts employee name, basic salary, and bonus percentage.
2. Calculates bonus(10% of basic salary)
3. Calculates HRA (20% of basic salary).
4. Calculates total salary.
5. Displays the employee details and salary breakdown.
Additional condition:
- Check whether the employee's total salary is greater than ₹50,000.
- Print the result as a Boolean value.
"""

employee_name = input("Employee Name: ")
basic_salary = int(input("Basic Salary: "))
bonus_percentage = int(input("Bonus Percentage: "))

employee_bonus = basic_salary * bonus_percentage / 100
employee_hra = basic_salary * 20 / 100
total_salary = basic_salary + employee_bonus + employee_hra

print(f"Employee Name: {employee_name}")
print(f"Basic Salary: {basic_salary}")
print(f"Bonus Percentage: {bonus_percentage}")
print(f"Bonus: {employee_bonus}")
print(f"HRA: {employee_hra}")
print(f"Total Salary: {total_salary}")

print(f"{total_salary > 50000}")