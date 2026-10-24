
# ============================================================
# DAY 1 - PYTHON FUNDAMENTALS
# STEP 3 - PRACTICE EXERCISES
# Total Marks: 10
# ============================================================


# ------------------------------------------------------------
# Q1. DATA TYPES AND TYPE CONVERSION (2 MARKS)
# ------------------------------------------------------------
# Given:
# quantity = "5"
# price = "199.50"
#
# Requirements:
# 1. Convert quantity into an appropriate numeric type.
# 2. Convert price into an appropriate numeric type.
# 3. Calculate and print the total cost.


# Write your solution below:
quantity = "5"
price = "199.50"
int_quantity = int(quantity)
float_price = float(price)
total_cost = int_quantity * float_price
print(total_cost)


# ------------------------------------------------------------
# Q2. ARITHMETIC OPERATORS (2 MARKS)
# ------------------------------------------------------------
# Given:
# total_items = 47
# items_per_box = 6
#
# Requirements:
# 1. Calculate the number of complete boxes.
# 2. Calculate the remaining items.
# 3. Calculate the total number of boxes required
#    to accommodate all items.
#
# Use arithmetic operators.


# Write your solution below:
total_items = 47
items_per_box = 6

complete_boxes = total_items // items_per_box
remaining_items = total_items % items_per_box
total_boxes = complete_boxes + 1

# ------------------------------------------------------------
# Q3. COMPARISON OPERATORS (2 MARKS)
# ------------------------------------------------------------
# Given:
# marks = 78
# passing_marks = 40
# maximum_marks = 100
#
# Requirements:
# 1. Check whether the student passed.
# 2. Check whether marks are greater than 75.
# 3. Check whether marks are within the valid range (0-100).
#
# Print the results as Boolean values.


# Write your solution below:
marks = 78
passing_marks = 40
maximum_marks = 100

print(marks > passing_marks)
print(marks > 75)
print(marks >= 0 and marks <= 100)


# ------------------------------------------------------------
# Q4. LOGICAL OPERATORS (2 MARKS)
# ------------------------------------------------------------
# Given:
# experience = 5
# has_python_knowledge = True
# has_java_knowledge = True
#
# Requirements:
# 1. Check whether the candidate has at least 3 years
#    of experience AND Python knowledge.
# 2. Check whether the candidate has Python OR Java knowledge.
# 3. Check whether the candidate has less than 2 years
#    of experience.
#
# Use logical operators.


# Write your solution below:
experience = 5
has_python_knowledge = True
has_java_knowledge = True

print(experience >= 3 and has_python_knowledge == True)
print(has_python_knowledge or has_java_knowledge)
print(experience < 2)


# ------------------------------------------------------------
# Q5. COMBINED CHALLENGE - PRODUCT BILLING (2 MARKS)
# ------------------------------------------------------------
# Given:
# product_price = 1200
# quantity = 3
# discount_percentage = 10
# gst_percentage = 18
#
# Requirements:
# 1. Calculate total price before discount.
# 2. Calculate discount amount.
# 3. Calculate price after discount.
# 4. Calculate GST on discounted price.
# 5. Calculate final payable amount.
#
# Print all five calculated values.


# Write your solution below:
product_price = 1200
quantity = 3
discount_percentage = 10
gst_percentage = 18

total_price = product_price * quantity
discount_amount = total_price * discount_percentage / 100 
gst_amount = (total_price - discount_amount) * 18 / 100
final_payment_amount = discount_amount + gst_amount
print(total_price)
print(discount_amount)
print(gst_amount)
print(final_payment_amount)

# ============================================================
# END OF DAY 1 - STEP 3
# ============================================================
