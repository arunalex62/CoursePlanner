import csv
import Course
import BSTNode
from tkinter import *
from tkinter import ttk
import json
from urllib.request import urlopen
import re

# math_courses = BSTNode.BSTNode(None)
# with open('math_courses.csv') as csv_file: 
#     csv_reader = csv.reader(csv_file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
#     for row in csv_reader:
#         courseToAdd = Course.Course(row[0], int(row[1]), row[2], row[3], (row[4]))
#         math_courses.insert(courseToAdd)

# window = Tk()

# window.title("SENG Course Planner")

# window.configure(width=500, height=300)
# window.configure(bg='lightgray')
# window.mainloop()


file = open('courses.json')
data = json.load(file)
for i in data['courses']:
    if(i['subjectCode']['name'] == "MATH"):
        print(i['__catalogCourseId'] + ", " + i['title'] + ", " + i['pid'])
        # url = "https://uvic.kuali.co/api/v1/catalog/course/5d9ccc4eab7506001ae4c225/" + i['pid']
        # page = urlopen(url)
        # html = page.read().decode("utf-8")
file.close()

url = "https://uvic.kuali.co/api/v1/catalog/course/5d9ccc4eab7506001ae4c225/HJe8yhOpX4"
page = urlopen(url)
course_info = json.loads(page.read())
print(re.sub('<[^<]+?>', '', course_info['preAndCorequisites']))
