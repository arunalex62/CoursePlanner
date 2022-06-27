import csv
import Course
import BSTNode

math_courses = BSTNode.BSTNode(None)
with open('math_courses.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in csv_reader:
        courseToAdd = Course.Course(row[0], int(row[1]), row[2], row[3], (row[4]))
        math_courses.insert(courseToAdd)
        courseToAdd.status()
