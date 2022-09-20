# data
#     student name
#     student id
#     student list
from fastapi import FastAPI

app = FastAPI()

student_list = [
    'Marcelle',
    'Bevan',
    'Anuj',
    'Kawana',
    'Ryan',
    'Kura',
    'Luke',
    'Kate',
    'Prerana',
    'Stacey',
    'Xavier',
    'Gracie',
    'Quentin',
    'Ben',
    'Raemon',
    'Dave',
    'Benke',
    'Jayam',
    'Will',
    'James',    
]

# functions
#     select random student
def select_random_student():
    # randomly select student
    pass

#     list of current students
@app.get("/students")
def current_students():
    return student_list

#     list of students who have shared
def shared_students():
    pass