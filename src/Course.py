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




    def add(self, course_subject, course_number): 
        csv_file = csv.reader(open('../courses/' + course_subject + '.csv', "r"), delimiter=",")

        for row in csv_file: 
            if(row[0] == course_subject and row[1] == course_number): 
                self.course_name = row[2]
                self.prerequisites = row[3]
                break


