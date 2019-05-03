import requests
import json
import pprint

saralUrl = "http://saral.navgurukul.org/api"


def saralRequest(Url):
    request = requests.get(Url)
    response = request.json()
    return response


coursesUrl = saralUrl+"/courses"
coursesResponse = saralRequest(coursesUrl)
# pprint.pprint (courses_response)

print("************************************Wel-Come in saral******************************")

listCourses = []
def coursesFunction():
    index = 0
    while index < len(coursesResponse["availableCourses"]):
        coursesEx = coursesResponse["availableCourses"][index]
        coursesName = coursesEx["name"]
        coursesId = coursesEx["id"]
        listCourses.append(coursesId)
        print index+0, coursesName, coursesId
        index = index + 1

coursesFunction()

print "............................................."

selectCourse = int(raw_input("Select The Course:-"))
selectCourseId = listCourses[selectCourse]
print(selectCourseId)


exerciseUrl = "{0}/{1}/exercises".format(coursesUrl, selectCourseId)

def exerciseFunction(exercise):
    index = 0
    id_list1 = []
    while(index < len(exercise['data'])):
        courses1=exercise['data'][index]
        
        course_id1=((courses1["slug"]))
        print (course_id1)
        id_list1.append(course_id1)
        index = index + 1

coursesResponse = saralRequest(exerciseUrl)
exerciseFunction(coursesResponse)