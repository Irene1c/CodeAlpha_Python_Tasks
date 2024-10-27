#!/usr/bin/env python3
"""STUDENT GRADE TRACKER"""


def gradetracker():
    """Function that tracks and calculates marks, average and % of student grades"""

    subjects = ['English', 'Kiswahili', 'Maths', 'Science', 'Social Studies', 'CRE']

    name = input("Student's Name: " )
    print(f"Student's name is: {name}\n")

    print("-------------------------------------------------")

    total = 0
    average = 0
    percentage = 0

    print("\nGRADES/MARKS PER SUBJECT OUT OF 50\n")

    for i in subjects:
        marks = input(f"{i} marks: " )
        print(f"{i} marks is {marks}/50")

        percentage = int(marks) * 2
        print(f"{i} percentage marks are {percentage}%")

        total = total + int(marks)
        print(f"Current total marks is {total}/300")

        average = total / 6
        print(f"Current average marks is {average:.2f}/50\n")

    print("-------------------------------------------------")

    print(f"Total marks for {name} is {total}/300")

    print(f"Average marks is {average:.2f}/50")

    avg_percentage = average * 2
    print(f"Average percentage is {avg_percentage:.2f}%")
    

if __name__=='__main__':

    print("STUDENT GRADE TRACKER\n")
    print("The following program tracks student grades and calculates their averages.")
    print("It allows users to input grades for different subjects.\n")

    gradetracker()
