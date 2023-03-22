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
        if(not prerequisites_met_recursive(course, student_course_list, course.prerequisites, student_year)):
            return False 
    return True

#Recursive function to determine whether the student has taken the prerequisites/corequisites
def prerequisites_met_recursive(course, student_course_list, prerequisite_string, student_year):
    #If the prerequisite string requires a minimum year standing, check if the student has met that year standing requirement.
    pattern = r"minimum\s(\w+)-year standing\."
    pattern2 = r"Minimum\s(\w+)-year standing\."
    if(re.match(pattern2, prerequisite_string) != None):
        pattern = pattern2
    if(re.match(pattern, prerequisite_string) != None): 
        required_year = re.search(pattern, prerequisite_string).group(1)
        if(required_year == "second" and student_year == 1):  
            print(f"You cannot take {course.course_subject} {course.course_number} because you have to be minimum second-year.")
            return False 
        elif(required_year == "third" and student_year <= 2): 
            print(f"You cannot take {course.course_subject} {course.course_number} because you have to be minimum third-year.")
            return False
        elif(required_year == "fourth" and student_year <= 3):
            print(f"You cannot take {course.course_subject} {course.course_number} because you have to be minimum fourth-year.")
            return False
        return True    
    if(prerequisite_string.startswith("Complete all of the following")):
        prerequisite_string = prerequisite_string[29:] 
        for req in prerequisite_string.split("Complete"):
            if(req == ""):
                continue
            #Returns false if any of the prerequisites are not met
            if req.strip() and not prerequisites_met_recursive(course, student_course_list, "Complete" + req, student_year):
                return False
        return True
    if(prerequisite_string.startswith("Complete 1 of the following")):
        prerequisite_string = prerequisite_string[27:]
        for req in prerequisite_string.split("Complete"):
            if(req == ""):
                continue
            #Returns true if any of the prerequisites are met
            if req.strip() and prerequisites_met_recursive(course, student_course_list, "Complete" + req, student_year):
                return True
        return False
    #Combined these two cases into the same if statement because they are similar
    elif(prerequisite_string.startswith("Complete 1 of:") or prerequisite_string.startswith("Completed or concurrently enrolled in 1 of:")): 
        prerequisite_courses = []
        #Checks which prerequisite string is being used
        concurrently = not prerequisite_string.startswith("Complete 1 of:")
        if(concurrently): 
            cutoff = 44
        else: 
            cutoff = 15
        for req in prerequisite_string[cutoff:].split(")"):
            if not req.strip() or req == "or permission of the department.":
                continue
            course_name = req.split(" ")[0]
            #Gets the course subject and number from the string
            course_subject = re.findall("[A-Z]+", course_name)[0]
            course_number = re.findall("[0-9]+", course_name)[0]
            prerequisite_courses.append((course_subject, course_number))
            #Returns true if the student has taken any of the prerequisites, since this is a "Complete 1 of" requirement
            if contains(student_course_list, add(course_subject, course_number)):
                return True
        #If this is a corequisite requirement, allow the student to take the course but mention the corequisite
        if(concurrently):
            print(f"You can take {course.course_subject} {course.course_number} if you enroll in any of ", end="")
            print(*[f"{c[0]} {c[1]}" for c in prerequisite_courses], sep=", ", end="")
            print(" concurrently.")
            return True
        #If the student has not taken any of the prerequisites, print out the courses that they need to take
        else:
            print(f"You cannot take {course.course_subject} {course.course_number} because you have not completed any of ", end="")
            print(*[f"{c[0]} {c[1]}" for c in prerequisite_courses], sep=", ", end="")
            print(".")
            return False
    elif(prerequisite_string.startswith("Complete all of:")): 
        for req in prerequisite_string[17:].split(")"):
            if not req.strip():
                continue
            #Checks if the prerequisite is a minimum year standing requirement, then calls the function recursively because there is a case to handle that.
            elif(req.startswith("minimum") or req.startswith("Minimum")): 
                return prerequisites_met_recursive(course, student_course_list, req, student_year)
            #Checks if the prereqyuiste is an admission to the program requirement, then returns true because there is no way to check if the student has met the "Admission to the Engineering program" requirement.
            elif(req.startswith("admission")): 
                return True
            course_name = req.split(" ")[0]
            #Gets the course subject and number from the string
            course_subject = re.findall("[A-Z]+", course_name)[0]
            course_number = re.findall("[0-9]+", course_name)[0]
            #Returns false if the student has not taken the prerequisite
            if not contains(student_course_list, add(course_subject, course_number)):
                print(f"You cannot take {course.course_subject} {course.course_number} because you have not completed ", end="")
                print(f"{course_subject} {course_number}.")
                return False
        return True
    #Returns true for those edge cases like "Chemistry 11 is a requirement" because that's a high school course that's not offered at UVic
    else: 
        return True
    

#Determines if the course provided has has been taken by the student.
def contains(self_course_list, course):
    return any((course.course_subject == i.course_subject and course.course_number == i.course_number) for i in self_course_list)

#Uses user input to fill the course list with the courses the student has taken.
def gather_courses():
    print("This program assumes you have completed all courses prior to the year you are in. Ex: If you are in 3rd year, you are assumed to have completed all 1st/2nd year courses.")
    print("Refer to your program's planning worksheet if needed: https://www.uvic.ca/ecs/_assets/docs/program-planning/PPW-SENG.pdf")
    
    self_course_list = []
    
    while True:
        student_year = input("What is your current year of study? (1/2/3/4)\n")
        if student_year in ["1", "2", "3", "4"]:
            break
        print("Please enter a valid year of study (1/2/3/4)\n")
    
    self_course_list = course_year_fill(self_course_list, int(student_year))
    
    while True:
        additional_courses = input(f"Have you completed any Year {student_year} courses? (y/n)\n").lower()
        if additional_courses in ["y", "n"]:
            break
        print("Please enter a valid response (y/n)\n")
    
    if additional_courses == "y":
        with open("seng_course_list.csv", "r") as f:
            csv_file = csv.reader(f, delimiter=",")
            next(csv_file) # skip the first line
            for row in csv_file:
                if int(row[4]) != int(student_year):
                    continue
                add_course = input(f"Have you taken {row[0]} {row[1]}? (y/n)\n").lower()
                while add_course not in ["y", "n"]:
                    add_course = input(f"Invalid Response: Have you taken {row[0]} {row[1]}? (y/n)\n").lower()
                if add_course == "y":
                    self_course_list.append(add(row[0], row[1]))
    
    print("=====================================================================")
    return self_course_list, student_year


