# Day 3: 30 Days of Python - Operators
# Name: Diya Starmon
# Staff: Sathish Kumar M

# 1. Variable declarations
age = 18
height = 5.7
complex_num = 1 + 2j

# 2. Area of a triangle (Area = 0.5 * b * h)
base = 20
h = 10
area_triangle = 0.5 * base * h
print("Area of the triangle:", area_triangle)

# 3. Perimeter of a triangle (side_a + side_b + side_c)
side_a = 5
side_b = 4
side_c = 3
perimeter_triangle = side_a + side_b + side_c
print("Perimeter of the triangle:", perimeter_triangle)

# 4. Rectangle area and perimeter
length = 10
width = 5
rect_area = length * width
rect_perimeter = 2 * (length + width)
print("Rectangle Area:", rect_area)
print("Rectangle Perimeter:", rect_perimeter)

# 5. Circle area and circumference (pi = 3.14)
pi = 3.14
radius = 7
circle_area = pi * (radius ** 2)
circle_circumference = 2 * pi * radius
print("Circle Area:", circle_area)
print("Circle Circumference:", circle_circumference)

# 6. Comparing lengths of 'python' and 'dragon'
len_python = len("python")
len_dragon = len("dragon")
print("len('python') != len('dragon'):", len_python != len_dragon)

# 7. Check if 'on' is in both 'python' and 'dragon' using 'and'
print("'on' in python and dragon:", ("on" in "python") and ("on" in "dragon"))

# 8. Check if 'jargon' is in the sentence using 'in'
sentence = "I hope this course is not full of jargon."
print("'jargon' in sentence:", "jargon" in sentence)

# 9. Find length of 'python', cast to float, then cast to string
str_len = len("python")
float_len = float(str_len)
str_from_float = str(float_len)
print("Converted to string:", str_from_float, type(str_from_float))

# 10. Check if a number is even
number = 14
print("Is 14 even?:", number % 2 == 0)

# 11. Floor division check: 7 // 3 == int(2.7)
print("7 // 3 == int(2.7):", (7 // 3) == int(2.7))

# 12. Type comparison: type('10') == type(10)
print("type('10') == type(10):", type("10") == type(10))

# 13. int check: int(float('9.8')) == 10
print("int(float('9.8')) == 10:", int(float("9.8")) == 10)