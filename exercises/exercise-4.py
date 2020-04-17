# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

triangle_a = int(input('''Enter the lengths of three side of a triangle:
a: '''))
triangle_b = int(input('b: '))
triangle_c = int(input('c: '))

if (triangle_a == triangle_b == triangle_c):
    print(f'A triangle with sides of {triangle_a}, {triangle_b} & {triangle_c} is an equalateral triangle')
elif (triangle_a != triangle_b and triangle_a != triangle_c and triangle_b != triangle_c):
    print(f'A triangle with sides of {triangle_a}, {triangle_b} & {triangle_c} is a scalene triangle')
else:
    print(f'A triangle with sides of {triangle_a}, {triangle_b} & {triangle_c} is a isosceles triangle')