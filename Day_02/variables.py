# Day 2: 30 Days of Python - Variables and Built-in Functions
# Name: Diya Starmon
# Staff: Sathish Kumar M

# Exercises: Level 1 - Declaring variables
first_name = "Diya"
last_name = "Starmon"
full_name = first_name + " " + last_name
country = "India"
city = "Ernakulam"
age = 18
year = 2026
is_married = False
is_true = True
is_light_on = True
skills = ["Python", "HTML", "C++"]

# Exercises: Level 2 - Using Built-in Functions
# 1. Checking data types
print("Data type of first_name:", type(first_name))
print("Data type of age:", type(age))
print("Data type of is_married:", type(is_married))
print("Data type of skills:", type(skills))

# 2. String length with len()
print("Length of first name:", len(first_name))
print("Is first name longer than last name?:", len(first_name) > len(last_name))

# 3. Basic arithmetic operations with variables
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Floor Division:", floor_division)

# 4. Circle calculations
radius = 30
area_of_circle = 3.14159 * (radius ** 2)
circum_of_circle = 2 * 3.14159 * radius
print("Area of circle:", area_of_circle)
print("Circumference of circle:", circum_of_circle)