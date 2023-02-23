import csv
import Course
import BSTNode
import API_Functions
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


# file = open('courses.json')
# with open('test.csv', 'w', newline='') as file1: 
#     writer = csv.writer(file1)
#     writer.writerow(["Department", "Number", "Description", "coAndPrerequisites"])
#     data = json.load(file)
#     for i in data['courses']:
#         if(i['subjectCode']['name'] == "MATH"):
#             url = "https://uvic.kuali.co/api/v1/catalog/course/5d9ccc4eab7506001ae4c225/HJe8yhOpX4"
#             page = urlopen(url)
#             course_info = json.loads(page.read())
#             print(i['__catalogCourseId'] + ", " + i['title'] + ", " + i['pid'])
#             writer.writerow(["MATH", re.sub('MATH', '', i['__catalogCourseId']), i['title'], re.sub('<[^<]+?>', '', course_info['preAndCorequisites'])])

# file.close()

# url = "https://uvic.kuali.co/api/v1/catalog/course/5d9ccc4eab7506001ae4c225/HJe8yhOpX4"
# page = urlopen(url)
# course_info = json.loads(page.read())
# print(re.sub('<[^<]+?>', '', course_info['preAndCorequisites']))

def main(): 
    # lst = [Course.Course() for i in range(100)]
    # test = input("Have you completed all First Year courses? (y/n)\n")
    # while(test != "y" and test != "n"):
    #      test = input("Please enter an input (y/n) if you have completed all First Year Courses\n")
    # if(test == "n"):
    #     test = "TEST"
    # elif(test == "y"): 
    #     print("hi")
    #     test = Course.Course()
    #     test.set("MATH", 100)
    #     test.fill()
    #     print(test.status())
    #     lst.append(test)
    #     #print(lst[0].status())
    API_Functions.Subject_CSV_Fill("PSYC")

if __name__ == "__main__": 
    main()