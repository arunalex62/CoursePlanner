import csv
import Course
import BSTNode
import API_Functions
from tkinter import *
from tkinter import ttk
import json
from urllib.request import urlopen
import re

def main(): 
    #subject = input("Please enter a course subject (such as MATH, ASTR, BIOL, etc).\n")  # Python 3
    #API_Functions.Subject_CSV_Fill(subject)
    seng_course_list = []
    seng_course_list = Course.seng_course_requirements_fill(seng_course_list)
    self_course_list = []
    completed = TRUE
    student_year = input("What is your current year of study? (1/2/3/4)\n")
    while(student_year != "1" and student_year != "2" and student_year != "3" and student_year != "4"):
        student_year = input("Please enter a valid year of study (1/2/3/4)\n")
    self_course_list = Course.course_year_fill(self_course_list, int(student_year)) 
    for course in seng_course_list: 
        if(not Course.contains(self_course_list, course) and Course.prerequisites_met(course, self_course_list)):
            print("You can take " + course.course_subject + " " + course.course_number + "!")
if __name__ == "__main__": 
    main()
    