import shutil
import random

class_in_progress = True

#start of loop
while class_in_progress:
#Check Length of student list
    studentfile = open('tempstudent.txt')
    studentfile.seek(0)
    first_char = studentfile.read(1)
#if list is empty them import from masterlist
    if not first_char:
        print('file was empty')
        shutil.copyfile('student.txt','tempstudent.txt')
#if file is not empty then close the txt file
    else:
        studentfile.close()
#request if we should randomly choose a student
        class_start = input("Should we start? (Y or N) ")
#if we want to proceed then open temp file
        if class_start == "y":
            studentfile = open('tempstudent.txt')
            students = studentfile.readlines()
            chr = '\n'
            students = [x.replace(chr, '') for x in students]
#choose student
            student = random.choice(students)
            print(student + " was chosen to share their screen")
            print("Those still awaiting to be chosen " + str(students))
#removes chosen student
            students.remove(student)
            students = [x.__add__('\n') for x in students]
#Open and write remaing students into tempstudent file
            studentfile = open('tempstudent.txt', 'w')
            studentfile.writelines(students)
            studentfile.close()
        elif class_start == "n":
            print("Goodbye")
            break
        else:
            print('Invalid respose. Please try again')

            