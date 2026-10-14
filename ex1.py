# module ex1
import random
import math
import sys

# TODO interactive bash script for inputs

def hello_python_exercises(student_name=["Bora TASCAN"]):
    if student_name == ["Bora TASCAN"]:
        print(f"This course has 1 student and one of them is {student_name[0]}")

    num_students = len(student_name)
    random_student = random.choice(student_name)
    print(f"This course has %i students and one of them is {random_student}" % num_students)

# hello_python_exercises()
student_name = ["Josias", "Bora", "Cornello", "Charlotte"]
hello_python_exercises(student_name=student_name)
