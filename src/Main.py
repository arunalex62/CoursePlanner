import Course

def main(): 
    #subject = input("Please enter a course subject (such as MATH, ASTR, BIOL, etc).\n")
    #API_Functions.Subject_CSV_Fill(subject)
    seng_course_list = []
    seng_course_list = Course.seng_course_requirements_fill(seng_course_list)
    self_course_list = []
    self_course_list, student_year = Course.gather_courses()
    for course in seng_course_list: 
        if(not Course.contains(self_course_list, course) and Course.prerequisites_met(course, self_course_list, int(student_year))):
            print("You can take " + course.course_subject + " " + course.course_number + "!")
if __name__ == "__main__": 
    main()
    