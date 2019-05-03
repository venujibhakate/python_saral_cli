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
# request1 = requests.get(exerciseUrl)
# response1 = request1.json()
# print response1
def exerciseFunction(exerciseData):
    index = 0
    exerciseList = []
    while(index < len(exerciseData['data'])):
        exercise = exerciseData['data'][index]
        
        exerciseName = exercise["name"]
        print (exerciseName)
        exerciseList.append(exerciseName)
        index = index + 1

coursesResponse = saralRequest(exerciseUrl)
exerciseFunction(coursesResponse)