class Course:
    course_subject = "Course Subject Unknown." 
    course_number = 0
    course_name = " Course Name Unknown."
    description = "Description not set."
    prerequisites = ""
    corequisites = ""

    def __init__(self, course_subject, course_number, course_name, description, prerequisites, corequisites):
        self.course_subject = course_subject 
        self.course_number = course_number
        self.course_name = course_name
        self.description = description
        self.prerequisites = prerequisites
        self.corequisites = corequisites

    def status(self):
        print(self.course_subject + " ", end = '') 
        print(self.course_number)
        print(self.course_name)
        print(self.description)
        if(len(self.prerequisites) == 0):
            print("Prerequisites: None")
        else:
            print("Prerequisites: " + self.prerequisites)
        if(len(self.corequisites) == 0):
            print("Corequisites: None")
        else:
            print("Corequisites: " + self.corequisites)
        print()

