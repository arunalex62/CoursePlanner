import csv
import json
from urllib.request import urlopen
import re

def Course_CSV_Fill(topic):
    file = open('courses.json')
    file_name = topic + '.csv'
    with open(file_name, 'w', newline='') as file1: 
        writer = csv.writer(file1)
        writer.writerow(["Department", "Number", "Description", "coAndPrerequisites"])
        data = json.load(file)
        for i in data['courses']:
            if(i['subjectCode']['name'] == topic):
                url = "https://uvic.kuali.co/api/v1/catalog/course/5d9ccc4eab7506001ae4c225/" + i['pid']
                page = urlopen(url)
                course_info = json.loads(page.read())
                print(i['__catalogCourseId'] + ", " + i['title'] + ", " + i['pid'])
                print(i['title'])
                try:
                    writer.writerow([topic, re.sub(topic, '', i['__catalogCourseId']), i['title'], re.sub('<[^<]+?>', '', course_info['preAndCorequisites'])])
                except KeyError as monkey:
                    try: 
                        writer.writerow([topic, re.sub(topic, '', i['__catalogCourseId']), i['title'], re.sub('<[^<]+?>', '', course_info['preOrCorequisites'])])
                    except KeyError as gorilla:
                        writer.writerow([topic, re.sub(topic, '', i['__catalogCourseId']), i['title'], ""])

        file.close()
