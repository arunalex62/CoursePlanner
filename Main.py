import csv
import Course

import BSTNode

math_courses = BSTNode.BSTNode(None)
with open('math_courses.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        courseToAdd = Course.Course(row[0], int(row[1]), row[2], row[3], row[4])
        type(courseToAdd.course_number)
        math_courses.insert(courseToAdd)
math_courses.course.status()