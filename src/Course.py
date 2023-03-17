import csv

class Course:
    course_subject = "Course Subject Unknown." 
    course_number = 0
    course_name = " Course Name Unknown."
    prerequisites = ""
    corequisites = ""

    def __init__(self):
        self.course_subject = "Course Subject Unknown."
        self.course_number = 0
        self.course_name =  "Course Name Unknown."
        self.prerequisites = ""
        self.corequisites = ""
    
    def set(self, course_subject, course_number):
        self.course_subject = course_subject
        self.course_number = course_number
        self.course_name =  "Course Name Unknown."
        self.prerequisites = ""
        self.corequisites = ""

    def status(self):
        print(self.course_subject + " ", end = '') 
        print(self.course_number)
        print(self.course_name)
        if(len(self.prerequisites) == 0):
            print("Prerequisites: None")
        else:
            print("Prerequisites: " + self.prerequisites)
        if(len(self.corequisites) == 0):
            print("Corequisites: None")
        else:
            print("Corequisites: " + self.corequisites)
        print()
    
    def fill(self): 
        csv_file = csv.reader(open("../courses/" + self.course_subject + ".csv", "r"), delimiter=",")
        for row in csv_file: 
            if(row[0] == self.course_subject and row[1] == self.course_number): 
                self.course_name = row[2]
                self.prerequisites = row[3]
                break


def add(course_subject, course_number): 
    course = Course()
    course.set(course_subject, course_number)
    csv_file = csv.reader(open('../courses/' + course_subject + '.csv', "r"), delimiter=",")

    for row in csv_file: 
        if(row[0] == course_subject and row[1] == course_number): 
            course.course_name = row[2]
            course.prerequisites = row[3]
            break
    return course

def seng_course_requirements_fill(seng_course_list): 
    csv_file = csv.reader(open("seng_course_list.csv", "r"), delimiter=",")
    firstLine = True
    for row in csv_file:
        if(firstLine): 
            firstLine = False
            continue
        seng_course_list.append(add(row[0], row[1]))
    return seng_course_list

def course_year_fill(list, year): 
    if(year == 0): 
        return list
    else: 
        csv_file = csv.reader(open("seng_course_list.csv", "r"), delimiter=",")
        firstLine = True
        for row in csv_file: 
            if(firstLine):
                firstLine = False
                continue
            if(int(row[4]) == year):
                list.append(add(row[0], row[1]))
        return course_year_fill(list, year-1)

def prerequisites_met(course, student_course_list):
    #Check if the course has prerequisites
    if(course != None and course.prerequisites != None or course.corequisites != None): 
        #Check if the student has taken the prerequisites/corequisites
        if(prerequisites_met_recursive(course, student_course_list, course.prerequisites) == False):
            return False 
    return True

#TODO: Fix this function 
#Recursive function to determine whether the student has taken the prerequisites/corequisites
def prerequisites_met_recursive(course, student_course_list, prerequisite_string):
    if(prerequisite_string.startswith("Complete all of the following")): 
        print("hi3") 
    elif(prerequisite_string.startswith("Complete 1 of:")): 
        prerequisite_string = prerequisite_string[16:] 
        print(prerequisite_string)
        return True
    return False

#Determines if the course provided as a parameter has been taken by the student.
def contains(self_course_list, course): 
    for i in range(len(self_course_list)):
        if(self_course_list[i].course_subject == course.course_subject and self_course_list[i].course_number == course.course_number): 
            return True
    return False


