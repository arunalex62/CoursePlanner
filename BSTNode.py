class BSTNode: 
    def __init__(self, course=None):
        self.left = None
        self.right = None
        self.course = course
    
    def insert(self, course):
        if self.course is None:
            self = course
            return
        elif(course.course_number > self.course_number):
            self.insert(self.right, course)
        else: 
            self.insert(self.left, course)