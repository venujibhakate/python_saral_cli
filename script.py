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
exerciseSlugList = []
def exerciseFunction(exerciseData):
    index = 0
    while(index < len(exerciseData['data'])):
        exercise = exerciseData['data'][index]
        exerciseName = exercise["name"]
        exerciseSlug = exercise["slug"]
        print index + 0,exerciseName,"***",exerciseSlug
        exerciseSlugList.append(exerciseSlug)
        index = index + 1
#     print exerciseSlugList

exerciseResponse = saralRequest(exerciseUrl)
exerciseFunction(exerciseResponse)

print "......................................................"
selectExercise = int(raw_input("Select the Exercise"))
selectExerciseId = exerciseSlugList[selectExercise]
print (selectExerciseId)



# slugUrl = selectCourse +"/"+ selectCourseId+ "/exercise/getBySlug?slug=" + selectExerciseId
# http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=requests__using-json
# slugUrl = coursesUrl"/"+(str(courses)+"/exercise/getBySlug")

slugUrl = "{0}/{1}/exercise/getBySlug?slug={2}".format(coursesUrl,selectCourseId,selectExerciseId,)
print(slugUrl)













# def contentAndchildEx(slug):



# slugResponse = saralRequest(slugUrl)
# contentAndchildEx(slugResponse)