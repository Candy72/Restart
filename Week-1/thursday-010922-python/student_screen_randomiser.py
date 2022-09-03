# Screen share randomizer!
# make a list of students
import random
studentfile = open('student.txt')
students = studentfile.readlines()
studentfile.close()
print(students)
students = students =  ['Ryan', 'Guilherme', 'Anuj', 'Gracie', 'Marcelle', 'Stacey', ' Ben', 'Bevan', 'Brandon', 'Crystal', 'Diana','James', 'Jayam', 'Luke', 'Kate', 'Kawana', 'Kura', 'Levi', 'Marc', 'Maria', 'Prerana', 'Victoria', 'Quentin', 'Sisi', 'Tia', 'Tina', 'Will', 'Xavier']

# Select a student from that list 
student = random.choice(students)

# Randomly remove from list 
students.remove(student)


studentfile = open('student.txt', "w")
studentfile.writelines(students)
studentfile.close()
# Tell user which student was chosen
print(student  + " has been chosen to share screen") 