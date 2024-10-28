#!/usr/bin/env python3
"""STUDENT GRADE TRACKER"""
import sys


def get_grade(perc_score):
    """Function that gets grade depending on percent score"""

    grade_ranges = [
    (80, 100, 'A'),
    (60, 79, 'B'),
    (50, 59, 'C'),
    (40, 49, 'D'),
    (0, 39, 'E')
    ]

    for lower, upper, grade in grade_ranges:
        if lower <= perc_score <= upper:
            return grade
    return None


def gradetracker():
    """Function that tracks and calculates marks, average and % of student grades"""

    subjects = ['English', 'Kiswahili', 'Maths', 'Science', 'Social Studies', 'CRE']

    name = input("Student's Name: " )
    print(f"Student's name is: {name}\n")

    print("-------------------------------------------------")

    total = 0
    average = 0
    percentage = 0

    print("\nINPUT MARKS PER SUBJECT OUT OF 50\n")

    try:
        for i in subjects:
            marks = input(f"{i} marks: " )
            print(f"{i} marks is {marks}/50")
            if int(marks) > 50:
                print("Invalid input: Each subject is out of 50")
                sys.exit() # Exit the program

            percentage = int(marks) * 2
            print(f"{i} percentage marks are {percentage}%")

            total = total + int(marks)
            print(f"Current total marks is {total}/300")

            average = total / 6
            print(f"Current average marks is {average:.2f}/50\n")

            grade = get_grade(percentage)
            print(f"{i} grade is: {grade}\n")

    except ValueError:
        print("Please enter a valid number.")
        sys.exit()

    print("-------------------------------------------------")

    print(f"Total marks for {name} is {total}/300")

    print(f"Average marks is {average:.2f}/50")

    avg_percentage = average * 2
    print(f"Average percentage is {avg_percentage:.2f}%\n")

    avg_grade = get_grade(avg_percentage)
    print(f"{name}'s average grade is: {avg_grade}\n")
    

if __name__=='__main__':

    print("STUDENT GRADE TRACKER\n")
    print("The following program tracks student grades and calculates their averages.")
    print("It allows users to input grades for different subjects.\n")

    gradetracker()
