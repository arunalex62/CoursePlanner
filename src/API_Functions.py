import csv
import json
from urllib.request import urlopen
import re
import Course

#Generates a csv file of all of the courses in a given subject and puts the file in the "courses" directory.
def Subject_CSV_Fill(topic):
    file = open('courses.json')
    file_name = "../courses/" + topic + '.csv'
    with open(file_name, 'w', newline='') as file1: 
        writer = csv.writer(file1)
        writer.writerow(["Department", "Number", "Description", "coAndPrerequisites"])
        data = json.load(file)
        for i in data['courses']:
            if(i['subjectCode']['name'] == topic):
                #This website is a student-made website for web-scraping UVic course data without having to make calls to UVic's official site.
                url = "https://uvic.kuali.co/api/v1/catalog/course/5d9ccc4eab7506001ae4c225/" + i['pid']
                page = urlopen(url)
                course_info = json.loads(page.read())
                #print statements here are just for debugging in terminal, and to see if the program is working correctly.
                print(i['__catalogCourseId'] + ", " + i['title'] + ", " + i['pid'])
                print(i['title'])
                #Exceptions for if a course has no PreOrCorequisites.
                try:
                    writer.writerow([topic, re.sub(topic, '', i['__catalogCourseId']), i['title'], re.sub('<[^<]+?>', '', course_info['preAndCorequisites'])])
                except KeyError as noPreAndCorequisites:
                    try: 
                        writer.writerow([topic, re.sub(topic, '', i['__catalogCourseId']), i['title'], re.sub('<[^<]+?>', '', course_info['preOrCorequisites'])])
                    except KeyError as noPreOrCorequisites:
                        writer.writerow([topic, re.sub(topic, '', i['__catalogCourseId']), i['title'], ""])

        file.close()
