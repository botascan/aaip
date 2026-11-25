# module ex1
import random
import math
import sys

# TODO interactive bash script for inputs
n = len(sys.argv)
l = []
for i in range(1,n):
    l.append(sys.argv[i])

def hello_python_exercises(student_names=["Bora"]):
    if student_names == ["Bora"]:
        print(f"This course has 1 student and one of them is {student_names[0]}")
    else:
        num_students = len(student_names)
        random_student = random.choice(student_names)
        print(f"This course has %i students and one of them is {random_student}" % num_students)

# hello_python_exercises()

hello_python_exercises(student_names=l)
