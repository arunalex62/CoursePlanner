import csv
import re 

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

    #Prints the course's information, pretty much like a toString() method.
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

    #Fill the rest of a course's information from the CSV file given the course's subject and course number.
    def fill(self): 
        csv_file = csv.reader(open("../courses/" + self.course_subject + ".csv", "r"), delimiter=",")
        for row in csv_file: 
            if(row[0] == self.course_subject and row[1] == self.course_number): 
                self.course_name = row[2]
                self.prerequisites = row[3]
                break

#Creates a new course object and fills it with all of its information from the CSV file, given the course's subject and course number.
def add(course_subject, course_number): 
    course = Course()
    course.set(course_subject, course_number)
    #"ELEC" is the old name for "ECE"
    if(course_subject == "ELEC" or course_subject == "CENG"): 
        course_subject = "ECE"
    csv_file = csv.reader(open('../courses/' + course_subject + '.csv', "r"), delimiter=",")

    for row in csv_file: 
        if(row[0] == course_subject and row[1] == course_number): 
            course.course_name = row[2]
            course.prerequisites = row[3]
            break
    return course
#Fills an empty list with course objects of each required course for the Software Engineering program. In the future, this will work for other programs.
def seng_course_requirements_fill(seng_course_list): 
    csv_file = csv.reader(open("seng_course_list.csv", "r"), delimiter=",")
    firstLine = True
    for row in csv_file:
        if(firstLine): 
            firstLine = False
            continue
        seng_course_list.append(add(row[0], row[1]))
    return seng_course_list
#Recursively fills a list with course objects of each course that are already taken by a student in the given year.
#Example: If a student says they are in their 3rd year, this function will fill the list with all of the courses they should have taken in their 1st and 2nd year.
def course_year_fill(list, year): 
    if(year == 1): 
        return list
    else: 
        csv_file = csv.reader(open("seng_course_list.csv", "r"), delimiter=",")
        firstLine = True
        for row in csv_file: 
            if(firstLine):
                firstLine = False
                continue
            if(int(row[4]) == year-1):
                list.append(add(row[0], row[1]))
        return course_year_fill(list, year-1)
#Checks if a student is able to take a given course based on their year and the courses they have already taken.
def prerequisites_met(course, student_course_list, student_year):
    #Check if the course has prerequisites
    if(course != None and course.prerequisites != None or course.corequisites != None): 
        #Check if the student has taken the prerequisites/corequisites
        if(prerequisites_met_recursive(course, student_course_list, course.prerequisites, student_year) == False):
            return False 
    return True

#Recursive function to determine whether the student has taken the prerequisites/corequisites
def prerequisites_met_recursive(course, student_course_list, prerequisite_string, student_year):
    pattern = r"minimum\s(\w+)-year standing\."
    pattern2 = r"Minimum\s(\w+)-year standing\."
    if(re.match(pattern2, prerequisite_string) != None):
        pattern = pattern2
    if(re.match(pattern, prerequisite_string) != None): 
        required_year = re.search(pattern, prerequisite_string).group(1)
        if(required_year == "second" and student_year == 1):  
            print("You cannot take " + course.course_subject + " " + course.course_number + " because you have to be minimum second-year.")
            return False 
        elif(required_year == "third" and student_year <= 2): 
            print("You cannot take " + course.course_subject + " " + course.course_number + " because you have to be minimum third-year.")
            return False
        elif(required_year == "fourth" and student_year <= 3):
            print("You cannot take " + course.course_subject + " " + course.course_number + " because you have to be minimum fourth-year.")
            return False
        return True   
    if(prerequisite_string.startswith("Complete all of the following")):
        prerequisite_string = prerequisite_string[29:] 
        complete_all_of = prerequisite_string.split("Complete") 
        for each in complete_all_of:  
            if(each == ""): 
               continue
            if(prerequisites_met_recursive(course, student_course_list, "Complete" + each, student_year) == False):
                return False
        return True
    if(prerequisite_string.startswith("Complete 1 of the following")):
        prerequisite_string = prerequisite_string[27:]
        complete_1_of = prerequisite_string.split("Complete") 
        for each in complete_1_of:  
            if(each == ""): 
               continue
            if(prerequisites_met_recursive(course, student_course_list, "Complete" + each, student_year) == True): 
                return True
        return False
        #print(prerequisite_string) 
        #print("hi3") 
    elif(prerequisite_string.startswith("Complete 1 of:")): 
        prerequisite_string = prerequisite_string[15:] 
        #print(prerequisite_string)
        prerequisite_courses = []
        while(prerequisite_string != ""): 
            if(prerequisite_string.startswith("or permission of the department.")):
                print("You cannot take " + course.course_subject + " " + course.course_number + " because you have not completed any of: ", end="")
                for i in range(len(prerequisite_courses)):
                    if(i == len(prerequisite_courses) - 1): 
                        print(prerequisite_courses[i][0] + " " + prerequisite_courses[i][1] + ".", end = "")
                    else:
                        print(prerequisite_courses[i][0] + " " + prerequisite_courses[i][1] + ", ", end = "")
                print()
                return False
            single_course = prerequisite_string.split(")")[0] +")"
            if(len(prerequisite_string.split(")", 1)[1]) > 0): 
                prerequisite_string = prerequisite_string.split(")", 1)[1]
            else:
                prerequisite_string = prerequisite_string = prerequisite_string.split(")")[1]
            #print("single_course:" + single_course + "\nprerequisite_string:" + prerequisite_string + "\n")
            course_name = single_course.split(" ")[0]
            #print("course_name:" + course_name)
            course_subject = re.findall("[A-Z]+", course_name)[0]
            course_number = re.findall("[0-9]+", course_name)[0]
            course_pair = (course_subject, course_number)
            prerequisite_courses.append(course_pair)
            if(contains(student_course_list, add(course_subject, course_number))): 
                return True
        print("You cannot take " + course.course_subject + " " + course.course_number + " because you have not completed any of ", end = "")
        for i in range(len(prerequisite_courses)):
            if(i == len(prerequisite_courses) - 1): 
                print(prerequisite_courses[i][0] + " " + prerequisite_courses[i][1] + ".", end = "")
            else:
                print(prerequisite_courses[i][0] + " " + prerequisite_courses[i][1] + ", ", end = "")
        print()
        return False
    elif(prerequisite_string.startswith("Complete all of:")): 
        prerequisite_string = prerequisite_string[17:]
        while(prerequisite_string != ""):  
            if(prerequisite_string.startswith("admission")):
                return True 
            if(prerequisite_string.startswith("minimum")):
                prerequisite_string = prerequisite_string.partition("standing")[0] + "standing."
                pattern = r"minimum\s(\w+)-year standing\."
            pattern = r"minimum\s(\w+)-year standing\."
            pattern2 = r"Minimum\s(\w+)-year standing\."
            if(re.match(pattern2, prerequisite_string) != None):
                pattern = pattern2
            if(re.match(pattern, prerequisite_string) != None): 
                required_year = re.search(pattern, prerequisite_string).group(1)
                if(required_year == "second" and student_year == 1):  
                    print("You cannot take " + course.course_subject + " " + course.course_number + " because you have to be minimum second-year.")
                    return False 
                elif(required_year == "third" and student_year <= 2): 
                    print("You cannot take " + course.course_subject + " " + course.course_number + " because you have to be minimum third-year.")
                    return False
                elif(required_year == "fourth" and student_year <= 3):
                    print("You cannot take " + course.course_subject + " " + course.course_number + " because you have to be minimum fourth-year.")
                    return False
                return True   
            single_course = prerequisite_string.split(")")[0] +")" 
            if(len(prerequisite_string.split(")")[1]) > 0): 
                prerequisite_string = prerequisite_string.split(")")[1] + ")" 
            else:
                prerequisite_string = prerequisite_string.split(")")[1] 
            course_name = single_course.split(" ")[0] 
            
            course_subject = re.findall("[A-Z]+", course_name)[0]
            course_number = re.findall("[0-9]+", course_name)[0]
            if(not contains(student_course_list, add(course_subject, course_number))): 
                print("You cannot take " + course.course_subject + " " + course.course_number + " because you have not completed " + course_subject + " " + course_number + ".")
                return False
            if(len(prerequisite_string) == 0): 
                return True
        return True 
    elif(prerequisite_string.startswith("Completed or concurrently enrolled in 1 of:")): 
        prerequisite_string = prerequisite_string[44:] 
        prerequisite_courses = []
        while(prerequisite_string != ""): 
            single_course = prerequisite_string.split(")")[0] +")"
            if(len(prerequisite_string.split(")")[1]) > 0): 
                prerequisite_string = prerequisite_string.split(")")[1] + ")" 
            else:
                prerequisite_string = prerequisite_string = prerequisite_string.split(")")[1]
            course_name = single_course.split(" ")[0]
            course_subject = re.findall("[A-Z]+", course_name)[0]
            course_number = re.findall("[0-9]+", course_name)[0]
            course_pair = (course_subject, course_number)
            prerequisite_courses.append(course_pair)
            if(contains(student_course_list, add(course_subject, course_number))): 
                return True
        print("You can take " + course.course_subject + " " + course.course_number + " if you enroll in any of ", end = "")
        for i in range(len(prerequisite_courses)):
            if(i == len(prerequisite_courses) - 1): 
                print(prerequisite_courses[i][0] + " " + prerequisite_courses[i][1] + " concurrently.", end = "")
            else:
                print(prerequisite_courses[i][0] + " " + prerequisite_courses[i][1] + ", ", end = "")
        print()
        return True 
    else: 
        return True
    

#Determines if the course provided has has been taken by the student.
def contains(self_course_list, course): 
    for i in range(len(self_course_list)):
        if(self_course_list[i].course_subject == course.course_subject and self_course_list[i].course_number == course.course_number): 
            return True
    return False

def gather_courses(): 
    self_course_list = []
    student_year = input("What is your current year of study? (1/2/3/4)\n")
    while(student_year != "1" and student_year != "2" and student_year != "3" and student_year != "4"):
        student_year = input("Please enter a valid year of study (1/2/3/4)\n")
    self_course_list = course_year_fill(self_course_list, int(student_year)) 
    return self_course_list, student_year


