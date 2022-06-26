class Course:
    course_subject = "Course Subject Unknown." 
    course_number = "Course Number Unknown."
    course_name = " Course Name Unknown."
    description = "Description not set."
    prerequisites = []

    def __init__(self, course_subject, course_number, course_name, description, prerequisites):
        self.course_subject = course_subject 
        self.course_number = course_number
        self.course_name = course_name
        self.description = description
        self.prerequisites = prerequisites

    def status(self):
        print(self.course_subject + " ", end = '') 
        print(self.course_number)
        print(self.course_name)
        print(self.description)
        if(self.prerequisites):
            print("Prerequisites: ", end = '') 
            for course in self.prerequisites:
                print(course.course_subject + " " + course.course_number, end = '') 
            print()


