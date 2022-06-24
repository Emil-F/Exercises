#Write your code below this line 👇
# def paint_calc(height, width, cover):
#     sum = test_h * test_w
#     calc = (sum // coverage) + (sum % coverage > 0)
#     print(f"You'll need {calc} cans of paint.")
import math
def paint_calc(height, width, cover):
    calc = (test_h * test_w / coverage)
    ceil = math.ceil(calc)
    print((f"You'll need {ceil} cans of paint."))
#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

