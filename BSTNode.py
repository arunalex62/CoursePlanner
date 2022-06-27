import Course
class BSTNode: 
    def __init__(self, course=None):
        self.left = None
        self.right = None
        self.course = course
    
    def insert(self, courseToAdd):
        if not self.course:
            self.course = courseToAdd
            return
        if (courseToAdd.course_number < self.course.course_number):
            if self.left: 
                self.left.insert(courseToAdd)
                return
            self.left = BSTNode(courseToAdd)
            return

        if(self.right):
            self.right.insert(courseToAdd) 
            return
        self.right = BSTNode(courseToAdd)

    def printInorder(self):
        if self:
            # First recur on left child
            self.printInorder(self.left)
    
            # then print the data of node
            print(self.course.status),
    
            # now recur on right child
            self.printInorder(self.right)