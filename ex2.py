# module ex2
import pandas as pd
import random
from faker import Faker

fake = Faker()

def csv_to_list(csv_file="students_list.csv"):
    """
    Turn a .csv file to a Python dict list
    """

    df = pd.read_csv(
        csv_file,
        header=None,
        names=["id", "name", "grade"],
        dtype={"id": int, "name": str, "grade": float})
    #print(df)
    return df.to_dict("records")

def next_id(database):
    """ Highest existing id + 1 """
    return max((s["id"] for s in database), default=0) + 1

def ask_grade(name):
    while True:
        try:
            grade = float(input(f"Input grade for {name} (eg. 1.7): "))
        except ValueError:
            print(f"Given Value not valid, try again for {name}: ")
            continue
        if not 1 <= grade <= 5:
            print(f"Grade given outside the scale, try again for {name}: ")
            continue
        return grade

def random_std_gen(n):
    
    return [{"id": 0,
            "name": fake.name(),
            "grade": random.uniform(1,5)}
            for _ in range(n)]

def add_students(database, st_list=None, n=None):
    """ 
    Take a 'database' and iteratively add new students 
    from a list and/or n random ones and/or interactively
    """
    
    if st_list is not None:
        new = st_list[:n]
    elif n is not None and n >= 1:
        new = random_std_gen(n)
    else:
        new = []
        while True:
            name = input("Give Student name (Entering Empty String exits): ").strip()
            if name == "":
                break
            grade = ask_grade(name)
            new.append({"id": 0, "name": name, "grade": grade})
    
    for student in new:
        database.append(**{student, "id", next_id(database)})
    return database

def print_std(student):
    print(f"ID: {student['id']:<5} | Name: {student['name']:<25} "
          f"| Grade: {student['grade']:.1f}")

def get_student(database, identifier=None, student_name=None):
    """
    Getter method for a student with ID, name or both)
    """
    if identifier is None and student_name is None:
        print("Give an id or name")
        return None
    for std in database:
        isvalid_id = identifier is None or std["id"] == identifier
        isvalid_name = student_name is None or std["name"].upper() == student_name.upper()

        if isvalid_id and isvalid_name:
            print_std(std)
            return std
    
    print("Student not found")
    return None

def set_grade(database, new_grade, identifier=None, student_name=None):
    
    student = get_student(database, identifier, student_name)

    if student is None:
        return False
    
    student["grade"] = float(new_grade)
    return True

def list_to_csv(database, filename="students_list.csv"):
    pd.DataFrame(database).to_csv(filename, header=False, index=False)

        