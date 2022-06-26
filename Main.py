import csv
from Course import Course

from BSTNode import BSTNode

math_courses = BSTNode()
with open('math_courses.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        course = Course(row[0], row[1], row[2], row[3], row[4])
        math_courses.insert(course)
