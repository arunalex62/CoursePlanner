import Course
class BSTNode: 
    def __init__(self, course=None):
        self.left = None
        self.right = None
        self.course = Course.Course
    
    def insert(self, courseToAdd):
        if self.course is None:
            print("hi")
            self = courseToAdd
            return
        elif(courseToAdd.course_number > self.course.course_number):
            self.right.insert(courseToAdd)
        else: 
            self.left.insert(courseToAdd)

    def printInorder(self):
        if self:
            # First recur on left child
            self.printInorder(self.left)
    
            # then print the data of node
            print(self.course.status),
    
            # now recur on right child
            self.printInorder(self.right)